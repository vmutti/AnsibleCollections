vmutti.vagrant.deploy
=====================

Copies the bundled `vagrant_project/` files to `vagrant_work_dir`, builds a `guests.json` describing every host in `vagrant_guest_group` (via `add_guest_config.yml`), and runs `vagrant up` for each guest.

Requirements
------------

`vagrant` (and `packer`, if guests are built from Packer boxes) must be installed on the hypervisor host. Run on a host acting as a Vagrant hypervisor.

Role Variables
--------------

`vagrant_binary_path`: path to the `vagrant` binary, default `/usr/bin/vagrant`.

`packer_binary_path`: path to the `packer` binary, default `/usr/bin/packer`.

`force_imports`: boolean, default `false`.

`vagrant_work_dir`: directory to write the generated Vagrant project into.

`vagrant_guest_group`: inventory group of hosts to generate Vagrant guest definitions for.

Dependencies
------------

N/A

Example Playbook
-----------------

    - hosts: vagrant_hypervisor
      vars:
        vagrant_work_dir: /home/ansible/vagrant
        vagrant_guest_group: vagrant_guest
      roles:
         - role: vmutti.vagrant.deploy

License
-------

MIT

Author Information
------------------

Shoshana Makinen, [blog.vmutti.com](https://blog.vmutti.com)
