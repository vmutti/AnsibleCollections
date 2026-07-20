vmutti.vault.server_db_create
=============================

Runs `vault operator init` against the running Vault server to create a new database, then parses out and prints the root token and unseal key(s). If Vault is already initialized, this is treated as a no-op rather than a failure.

Requirements
------------

A running, uninitialized Vault server reachable at `http://127.0.0.1:<vault_server_port>`.

Role Variables
--------------

`vault_server_port`: port the local Vault server is listening on.

Dependencies
------------

N/A

Example Playbook
-----------------

    - hosts: vault_server
      vars:
        vault_server_port: 8200
      roles:
         - role: vmutti.vault.server_db_create

License
-------

MIT

Author Information
------------------

Shoshana Makinen, [blog.vmutti.com](https://blog.vmutti.com)
