vmutti.chrome.install
=====================

Installs Google Chrome (stable channel) directly from Google's official `.deb` package.

Requirements
------------

Debian-based distro with apt. The target host must be a member of the `host_install_chrome` group.

Role Variables
--------------

This role has no configurable variables.

Dependencies
------------

N/A

Example Playbook
-----------------

    - hosts: host_install_chrome
      roles:
         - role: vmutti.chrome.install

License
-------

MIT

Author Information
------------------

Shoshana Makinen, [blog.vmutti.com](https://blog.vmutti.com)
