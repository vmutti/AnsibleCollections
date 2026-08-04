vmutti.libvirt_guest.install
=============================

Installs the `qemu-guest-agent` package via apt and enables/starts the `qemu-guest-agent` service, so the libvirt host can query guest info (IP addresses, etc.) and manage the VM (clean shutdown, filesystem freeze/thaw for snapshots) without relying solely on the network.

Requirements
------------

Debian-based distro with apt. The target host must be a libvirt guest and a member of the `host_install_libvirt_guest` group.

Role Variables
--------------

This role has no configurable variables.

Dependencies
------------

N/A

Example Playbook
-----------------

    - hosts: host_install_libvirt_guest
      roles:
         - role: vmutti.libvirt_guest.install

License
-------

MIT

Author Information
------------------

Shoshana Makinen, [blog.vmutti.com](https://blog.vmutti.com)
