vmutti.libvirt.install
=======================

Installs `qemu-kvm`, `libvirt-daemon-system`, `libvirt-clients`, and related tooling via apt, enables/starts the `libvirtd` service, and adds configured users to the `libvirt` and `kvm` groups so they can manage VMs without root.

Requirements
------------

Debian-based distro with apt. The target host must be a member of the `host_install_libvirt` group.

Role Variables
--------------

`libvirt_packages`: list of apt packages to install, default `qemu-kvm`, `libvirt-daemon-system`, `libvirt-clients`, `bridge-utils`, `virtinst`, `ovmf`.

`libvirt_usernames`: list of usernames to add to the `libvirt` and `kvm` groups.

Dependencies
------------

N/A

Example Playbook
-----------------

    - hosts: host_install_libvirt
      vars:
        libvirt_usernames:
          - ansible
      roles:
         - role: vmutti.libvirt.install

License
-------

MIT

Author Information
------------------

Shoshana Makinen, [blog.vmutti.com](https://blog.vmutti.com)
