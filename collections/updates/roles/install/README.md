vmutti.updates.install
======================

Runs `apt update` followed by a dist-upgrade of all packages (including recommends), and removes packages that are no longer needed.

Requirements
------------

Debian-based distro with apt.

Role Variables
--------------

This role has no configurable variables.

Dependencies
------------

N/A

Example Playbook
-----------------

    - hosts: all
      roles:
         - role: vmutti.updates.install

License
-------

MIT

Author Information
------------------

Shoshana Makinen, [blog.vmutti.com](https://blog.vmutti.com)
