vmutti.scoutsuite.install
=========================

Installs the [ScoutSuite](https://github.com/nccgroup/ScoutSuite) Python package via pip for multi-cloud (AWS/Azure/GCP) security auditing.

Requirements
------------

A working `pip` on the target host.

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
         - role: vmutti.scoutsuite.install

License
-------

MIT

Author Information
------------------

Shoshana Makinen, [blog.vmutti.com](https://blog.vmutti.com)
