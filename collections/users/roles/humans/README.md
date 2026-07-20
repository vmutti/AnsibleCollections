vmutti.users.humans
===================

Creates a local user account (with a home directory and `sudo` group membership) for each username in `human_usernames`, when `host_setup_human_users` is true.

Requirements
------------

None.

Role Variables
--------------

`host_setup_human_users`: boolean. Must be true for accounts to be created (see `vmutti.users.common`).

`human_usernames`: list of usernames to create as local sudo-capable accounts.

Dependencies
------------

N/A

Example Playbook
-----------------

    - hosts: all
      vars:
        host_setup_human_users: true
        human_usernames:
          - ansible
      roles:
         - role: vmutti.users.humans

License
-------

MIT

Author Information
------------------

Shoshana Makinen, [blog.vmutti.com](https://blog.vmutti.com)
