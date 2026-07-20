vmutti.vault.common
===================

Provides shared default variables consumed by the other roles in this collection. Has no tasks of its own.

Requirements
------------

None.

Role Variables
--------------

Currently defines no defaults of its own; reserved for shared variables used by sibling vault roles.

Dependencies
------------

N/A

Example Playbook
-----------------

    - hosts: vault_server
      roles:
         - role: vmutti.vault.common

License
-------

MIT

Author Information
------------------

Shoshana Makinen, [blog.vmutti.com](https://blog.vmutti.com)
