class Guest
  def initialize(globalvagrant, config, vb_callbacks=[], lv_callbacks=[], vm_callbacks=[], callbacks=[])
    # stow away the vagrant handle and the input guest config
    @globalvagrant = globalvagrant
    @config = config
    @vb_callbacks = vb_callbacks
    @lv_callbacks = lv_callbacks
    @vm_callbacks = vm_callbacks
    @callbacks = callbacks

    # Check mandatory configs
    @name = @config.has_key?("name") ? @config['name'] : raise("must provide name for machine")
    @box = @config.has_key?("box_name") ? @config['box_name'] : raise("must provide box to use for #{@name}") 
    @ssh_private_key_path = @config.has_key?("ssh_private_key_path") ? @config['ssh_private_key_path'] : raise("must provide ssh_private_key_path for #{@name}") 
    

    # Optional configs
    @storage_path = @config.has_key?("storage_path") ? @config['storage_path'] : ""

    if @config.has_key?("workspace_path") 
      setup_workspace_dir(@config['workspace_path'])
    end


    @username = @config.has_key?("username") ? @config['username'] : 'vagrant'
    @autostart = @config.has_key?("autostart") ? @config['autostart'] : false
    @home_path = @config.has_key?("home_path") ? @config['home_path'] : "/home/#{@username}"


    # install dependencies and do initial configuration
    run_provisioner("pre_install.sh")


    # machine configurations
    @config.has_key?("cpu_cores") ? setup_cpus(@config['cpu_cores']) : setup_cpus()
    @config.has_key?("virt_provider") ? setup_virt_provider(@config['virt_provider']) : setup_virt_provider()
    @config.has_key?("nested_virt") ? setup_nested_virt(@config['nested_virt']) : setup_nested_virt()
    @config.has_key?("memory_MBs") ? setup_memory(@config['memory_MBs']) : setup_memory()



    if @config.has_key?("gui") and @config['gui']
      @config.has_key?("vram_MBs") ? setup_graphics(@config['vram_MBs']) : setup_graphics()
    end

    @graphics_controller_set = @config.has_key?("graphics_controller") ? @config['graphics_controller'] : "vmsvga"
    setup_graphics_controller(@graphics_controller_set)

    @rdp_enable = @config.has_key?("rdp") ? @config['rdp'] : false
    setup_rdp(@rdp_enable)

    @usb_enable = @config.has_key?("usb") ? @config['usb'] : true
    setup_usb(@usb_enable)

    if @config.has_key?("networks")
      @config['networks'].each do |network|
        setup_network(network)
      end
    end

    if @config.has_key?("shared_folders")
      @config['shared_folders'].each do |shared_folder|
        sync_dir(shared_folder['src'],shared_folder['name'])
      end
    end

    if @config.has_key?("storage")
      @config['storage'].each do |storage|
        setup_storage(storage)
      end
    end

    if @config.has_key?("portfwds")
      @config['portfwds'].each do |portfwd|
        setup_portfwd(portfwd)
      end
    end

    # Actually define and provision machine
    @globalvagrant.vm.define @name, autostart: @autostart do |vagrant|
      run_provisioner("post_install.sh")
      vagrant.vm.box = @box
      vagrant.vm.hostname = @name.gsub(/\//,'-')
      vagrant.ssh.private_key_path = @ssh_private_key_path
      vagrant.ssh.username = @username
      vagrant.ssh.keys_only = true
      vagrant.ssh.insert_key = false
      vagrant.ssh.dsa_authentication = false
      vagrant.ssh.verify_host_key = :accept_new_or_local_tunnel
      vagrant.vm.synced_folder ".", "/vagrant", disabled: true
      if @config['provider']=='virtualbox'
        vagrant.vm.provider "virtualbox" do |vbox|
          vbox.check_guest_additions = false
          vbox.name = @name.gsub(/\//,'-')

          vbox.customize ["modifyvm", :id, "--clipboard-mode", "bidirectional"]
          vbox.customize ["modifyvm", :id, "--ioapic", "on"]
          vbox.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
          @vb_callbacks.each do |cb|
            cb.call(vbox)
          end
        end
      elsif @config['provider']=='libvirt'
        vagrant.vm.provider :libvirt do |libvirt|
          libvirt.socket='/run/libvirt/libvirt-sock'
          @lv_callbacks.each do |cb|
            cb.call(libvirt)
          end
        end
      end
      @vm_callbacks.each do |cb|
        cb.call(vagrant.vm)
      end
      @callbacks.each do |cb|
        cb.call(vagrant)
      end
    end
  end

  def vm(&cb)
    @vm_callbacks.push(cb)
  end

  def vb(&cb)
    @vb_callbacks.push(cb)
  end

  def lv(&cb)
    @lv_callbacks.push(cb)
  end

  def callback(&cb)
    @callbacks.push(cb)
  end

  def setup_network(network)
    interface = network.has_key?("interface") ? network['interface'] : "VirtualBox Host-Only Ethernet Adapter"
    ip = network.has_key?("ip") ? network['ip'] : raise("Networks must specify an IP")

    vm() do |vmach|
      vmach.network "private_network", name: interface,  ip: ip
    end
  end

  def setup_portfwd(portfwd)
    host_ip = portfwd.has_key?("host_ip") ? portfwd['host_ip'] : '127.0.0.1'
    setup_rdp(@rdp_enable)
    vm() do |vmach|
      vmach.network "forwarded_port", host: portfwd['host_port'], guest: portfwd['guest_port'], host_ip: host_ip
    end
  end

  def setup_graphics(vram=96)
    vb() do |vbox|
      vbox.gui = true
      vbox.customize ["modifyvm", :id, "--vram", vram]
    end
  end

  def setup_graphics_controller(graphics_controller="vmsvga")
    vb() do |vbox|
      vbox.gui = true
      vbox.customize ["modifyvm", :id, "--graphicscontroller", graphics_controller]
    end
  end

  def setup_memory(memory=4096)
    vb() do |vbox|
      # vmox.memory = memory
      vbox.customize ["modifyvm", :id, "--memory", memory]
    end
    lv() do |libv|
      libv.memory = memory
    end
  end

  def setup_cpus(cpus=1)
    vb() do |vbox|
      # vbox.cpus=cpus
      vbox.customize ["modifyvm", :id, "--cpus", cpus]
    end
    lv() do |libv|
      libv.cpus=cpus
      libv.cpu_model='qemu64'
    end
  end

  def setup_rdp(enable=false)
    vb() do |vbox|
      vbox.customize ["modifyvm", :id, "--vrdeauthtype", "external"]
      vbox.customize ["modifyvm", :id, "--vrde", enable ? "on" : "off" ] 
    end
  end

  def setup_usb(enable=true)
    vb() do |vbox|
      vbox.customize ["modifyvm", :id, "--usb", enable ? "on" : "off"]
      vbox.customize ["modifyvm", :id, "--usbehci", enable ? "on" : "off"]
    end
  end

  def setup_virt_provider(provider='default')
    vb() do |vbox|
      vbox.customize ["modifyvm", :id, "--paravirtprovider", provider]
    end
  end

  def setup_nested_virt(enable=false)
    vb() do |vbox|
      vbox.customize ["modifyvm", :id, "--nested-hw-virt", enable ? "on" : "off"]
    end
  end

  def sync_dir(src,name,owner,group,mode)
    require 'fileutils'
    FileUtils.mkdir_p src
    vm() do |vmach|
      vmach.synced_folder src, "/#{name}", automount:true, owner:owner, group:group, mount_options:['dmode='+mode,'fmode='+mode]
    end
  end

  def setup_workspace_dir(workspace_path)
    sync_dir(workspace_path,"workspace",'root','vboxsf','770')
    run_inline("mount workspace","if [ ! -e  $HOME/workspace ]; then ln -f -s /media/sf_workspace $HOME/workspace;  fi")
  end

  def copy(src, dst)
    if (File.exist?(src))
      vm do |vmach|
        vmach.provision "file", source: src, destination: dst
      end
    else
      puts "Could not find a file named: #{src} to copy to guest"
    end
  end

  def run_path(name, path, args=[])
    vm() do |vmach|
      vmach.provision name, privileged: false, type:"shell", path: path, args: args, env:{"HOME" => @home_path}
    end
  end

  def run_inline(name, command)
    vm do |vmach|
      vmach.provision "shell", inline: command, env:{"HOME" => @home_path}
    end
  end

  def run_provisioner(path, args=[])
    run_path("#{path}", "./provisioners/#{path}",args)
  end

  def setup_storage_drive(path, size=10240)
    disk_path = "#{@storage_path}/#{@name}/#{path}.vdi"
    if !(File.exist?("C:#{disk_path}") )
      require 'fileutils'
      FileUtils.mkdir_p File.dirname(disk_path)
      vb() do |vbox|
        vbox.customize ["createmedium", "disk", "--filename", disk_path, "--size", size.to_s]
      end
    end
    vb() do |vbox|
      vbox.customize ["storageattach", :id, "--storagectl","IDE Controller","--port","1","--device","1","--type","hdd", "--medium",disk_path]
    end
    run_provisioner("storage_install.sh")
  end

end

