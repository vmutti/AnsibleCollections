vmutti.users.common
===================

Provides shared default variables consumed by the other roles in this collection. Has no tasks of its own; include it (or set its defaults) so `vmutti.users.humans` and `vmutti.users.virtualbox_shared_folders` know whether to act.

Requirements
------------

None.

Role Variables
--------------

`host_setup_human_users`: boolean, default `false`. Gates `vmutti.users.humans`.

`host_setup_virtualbox_users`: boolean, default `false`. Gates `vmutti.users.virtualbox_shared_folders`.

Dependencies
------------

N/A

Example Playbook
-----------------

    - hosts: all
      vars:
        host_setup_human_users: true
      roles:
         - role: vmutti.users.common

License
-------

MIT

Author Information
------------------

Shoshana Makinen, [blog.vmutti.com](https://blog.vmutti.com)
