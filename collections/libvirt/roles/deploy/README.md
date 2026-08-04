vmutti.libvirt.deploy
======================

Deploys libvirt storage pools, networks, and guest domains on a libvirt hypervisor host using the `community.libvirt` collection modules (`virt_pool`, `virt_net`, `virt`).

Pools and networks are generated from dictionary variables set on the hypervisor host itself. Guest domains are generated from inventory: any host in `libvirt_guest_group` whose `libvirt_hypervisor` variable identifies this hypervisor gets defined (and started) here, the same way `vmutti.vagrant.deploy` builds Vagrant guest configs from a guest group.

Requirements
------------

`community.libvirt` (and its requirements, `python3-libvirt` and `python3-lxml`) must be installed on the hypervisor host. Run on a host acting as a libvirt hypervisor — see `vmutti.libvirt.install` for installing libvirt/QEMU-KVM itself.

Role Variables
--------------

`libvirt_uri`: libvirt connection URI, default `qemu:///system`.

`libvirt_guest_group`: inventory group containing every libvirt guest across all hypervisors, default `libvirt_guests`.

`libvirt_hypervisor_identifier`: the value guests must set in their `libvirt_hypervisor` variable to be deployed onto this host, default `{{ inventory_hostname }}`.

`libvirt_guest_default_state`: state guest domains are put into when a guest doesn't set its own `libvirt_state`, default `running`.

### Pools and networks

Set on the hypervisor host (or a group it belongs to). Every hostvar matching `^libvirt_pool_.*$` becomes one storage pool; every hostvar matching `^libvirt_net_.*$` becomes one network. The variable name itself is arbitrary (only the prefix is matched) — use it to give each definition a distinct key.

    libvirt_pool_images:
      name: images
      type: dir
      target_path: /var/lib/libvirt/images/guests
      autostart: true

    libvirt_net_guests:
      name: guests
      forward_mode: nat
      bridge_name: virbr-guests
      domain_name: guests.local
      ip:
        address: 192.168.122.1
        netmask: 255.255.255.0
        dhcp_range:
          start: 192.168.122.10
          end: 192.168.122.200

Pool keys: `name` (required), `type` (default `dir`), `uuid`, `target_path`, `permissions.{owner,group,mode}`, `source.{host,dir,device,name,format}`, `autostart` (default `true`), `build` (default `true`, set `false` to skip the `virt_pool` build command for pool types that don't support/need it).

Network keys: `name` (required), `uuid`, `forward_mode` (omit for an isolated network), `bridge_name`, `stp`, `delay`, `domain_name`, `ip.{address,netmask}`, `ip.dhcp_range.{start,end}`, `ip.dhcp_hosts` (list of `{mac, name, ip}`), `autostart` (default `true`).

### Guest domains

Each guest is an inventory host in `libvirt_guest_group`. Its own hostvars, any key matching `^libvirt_.*$`, are collected and the `libvirt_` prefix stripped to build the domain definition — the same pattern `vmutti.vagrant.deploy` uses for `vagrant_*` guest vars.

`libvirt_hypervisor` (required): identifies which hypervisor should deploy this guest — must equal that hypervisor's `libvirt_hypervisor_identifier` (its `inventory_hostname` by default).

    libvirt_hypervisor: dev.Thiala.local.vmutti.com
    libvirt_memory_mb: 2048
    libvirt_vcpus: 2
    libvirt_disk_path: /var/lib/libvirt/images/guests/example.qcow2
    libvirt_network: guests
    libvirt_autostart: true

Other guest keys: `uuid`, `memory_mb` (default `1024`), `vcpus` (default `1`), `arch` (default `x86_64`), `machine` (default `pc`), `boot_dev` (default `hd`), `disk_path`, `disk_format` (default `qcow2`), `disk_bus` (default `virtio`), `cdrom_path`, `network` (default `default`), `mac`, `nic_model` (default `virtio`), `graphics_type` (default `vnc`), `graphics_listen` (default `0.0.0.0`), `video_model` (default `qxl`), `autostart` (default `false`), `state` (default `libvirt_guest_default_state`).

### Disk image upload

If a guest sets `image_path` alongside `disk_path`, the role copies the qcow2 (or other disk image) at `image_path` — resolved on the Ansible controller, e.g. a Packer build under `PackerImages/builds/<location>/<stage>/<image>/libvirt/<image>` — to `disk_path` on the hypervisor before domains are defined, creating `disk_path`'s parent directory first if needed. The `copy` module skips the transfer on later runs when the destination already matches. Omit `image_path` for guests whose disk is provisioned some other way.

    libvirt_image_path: "{{ libvirt_images_path }}/worchestation-debian-libvirt/libvirt/worchestation-debian-libvirt"
    libvirt_disk_path: /var/lib/libvirt/images/guests/example.qcow2

Dependencies
------------

`community.libvirt`

Example Playbook
-----------------

    - hosts: "{{ target_hosts | default('all') }}:&libvirt_hypervisor"
      roles:
        - vmutti.libvirt.deploy

Run against a single hypervisor with `-e target_hosts=dev.Thiala.local.vmutti.com` (or `--limit`); the role only defines guests whose `libvirt_hypervisor` matches the hypervisor(s) actually being played.

License
-------

MIT

Author Information
------------------

Shoshana Makinen, [blog.vmutti.com](https://blog.vmutti.com)
