vmutti.vault.server_vault_command
=================================

Runs an arbitrary `vault` CLI command (`vault_argv`) against `vault_address`, authenticating with `vault_token`. A low-level building block used by the other setup/unseal roles in this collection.

Requirements
------------

The `vault` binary must be available at `vault_binary_path` on the target host.

Role Variables
--------------

`vault_binary_path`: path to the `vault` binary.

`vault_argv`: list of CLI arguments to pass to `vault` (excluding the binary itself).

`vault_address`: value for the `VAULT_ADDR` environment variable.

`vault_token`: value for the `VAULT_TOKEN` environment variable.

Dependencies
------------

N/A

Example Playbook
-----------------

    - hosts: vault_server
      vars:
        vault_address: http://127.0.0.1:8200
        vault_argv: ['status']
      roles:
         - role: vmutti.vault.server_vault_command

License
-------

MIT

Author Information
------------------

Shoshana Makinen, [blog.vmutti.com](https://blog.vmutti.com)
