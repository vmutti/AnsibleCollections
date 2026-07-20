vmutti.vault.server_db_init
===========================

Runs a `vault` CLI command against the local server and delegates to `vmutti.podman.server_vault_command`, as part of initial database setup. This role is still a work in progress.

Requirements
------------

A running Vault server, and the `vmutti.podman` collection installed.

Role Variables
--------------

`vault_server_version` / `vault_server_arch` / `vault_server_checksum`: pinned Vault release used elsewhere in server setup, default `1.6.2` / `linux_amd64`.

`vault_server_host_prerequisites`: OS packages required on the host, default `['unzip']`.

`vault_server_user` / `vault_server_group`: OS user/group Vault runs as, default `vault`/`vault`.

`vault_server_config_path`: path to the Vault config file, default `/etc/vault.hcl`.

`vault_server_storage_path`: path to the Vault storage directory, default `/var/vault`.

`vault_server_port`: port the local Vault server is listening on.

Dependencies
------------

vmutti.podman

Example Playbook
-----------------

    - hosts: vault_server
      roles:
         - role: vmutti.vault.server_db_init

License
-------

MIT

Author Information
------------------

Shoshana Makinen, [blog.vmutti.com](https://blog.vmutti.com)
