vmutti.packer.build
===================

For each guest host in `packer_guest_group`, merges builder/provisioner/post-processor configuration fragments (default, then platform/distro/packager, then any profiles) from `controller_packer_config_dir`, writes the resulting Packer JSON config and variables file, and kicks off `packer build` asynchronously. Waits for all launched builds to finish.

Requirements
------------

The `packer` binary must be installed on the target host (see `packer_binary_path`). Intended to run on a Vagrant/Packer hypervisor host.

Role Variables
--------------

`packer_binary_path`: path to the `packer` binary, default `/usr/bin/packer`.

`packer_become` / `packer_become_user`: privilege escalation used when running the async `packer build` job, default `no` / `root`.

`packer_guest_group`: inventory group of guest hosts to build images for.

`controller_packer_config_dir`: directory on the controller holding default/platform/distro/packager/profile Packer config fragments.

Dependencies
------------

N/A

Example Playbook
-----------------

    - hosts: vagrant_hypervisor
      vars:
        packer_guest_group: vagrant_guest
      roles:
         - role: vmutti.packer.build

License
-------

MIT

Author Information
------------------

Shoshana Makinen, [blog.vmutti.com](https://blog.vmutti.com)
