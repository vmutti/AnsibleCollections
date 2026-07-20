vmutti.vault.server_db_destroy
==============================

Stops the Vault server (via the role named in `vault_server_manage_role`), then, if explicitly confirmed, permanently deletes the Vault storage directory. This is a destructive operation gated behind an explicit confirmation flag.

Requirements
------------

None beyond a stoppable Vault server. Deletion only happens when `vault_server_db_destroy_confirm` is `true`.

Role Variables
--------------

`vault_server_db_destroy_confirm`: boolean, default `false`. Must be explicitly set to `true` to actually delete the storage directory.

`vault_server_manage_role`: fully-qualified role name used to stop the Vault server (e.g. `vmutti.vault.podman_server_manage`).

`vault_hypervisor_storage_path`: path to the Vault storage directory to delete.

Dependencies
------------

N/A

Example Playbook
-----------------

    - hosts: vault_hypervisor
      vars:
        vault_server_manage_role: vmutti.vault.podman_server_manage
        vault_server_db_destroy_confirm: true
      roles:
         - role: vmutti.vault.server_db_destroy

License
-------

MIT

Author Information
------------------

Shoshana Makinen, [blog.vmutti.com](https://blog.vmutti.com)
