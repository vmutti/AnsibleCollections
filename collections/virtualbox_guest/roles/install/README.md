vmutti.virtualbox_guest.install
===============================

Includes a distro-specific task file (`{{ ansible_distribution | lower }}.yml`; Debian and Kali are provided) that installs VirtualBox Guest Additions — on Debian by mounting the Guest Additions ISO and running its installer, on Kali by installing the `virtualbox-guest-x11` package.

Requirements
------------

The target host must be a VirtualBox guest and a member of the `host_install_virtualbox_guest` group. A task file for the host's `ansible_distribution` must exist in this role.

Role Variables
--------------

This role has no configurable variables.

Dependencies
------------

N/A

Example Playbook
-----------------

    - hosts: host_install_virtualbox_guest
      roles:
         - role: vmutti.virtualbox_guest.install

License
-------

MIT

Author Information
------------------

Shoshana Makinen, [blog.vmutti.com](https://blog.vmutti.com)
