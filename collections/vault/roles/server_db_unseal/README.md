vmutti.vault.server_db_unseal
=============================

Unseals the Vault server using `vault_server_unseal_keys` if set. If the server is still sealed afterward, interactively prompts for comma-separated unseal keys and retries.

Requirements
------------

A running, initialized Vault server reachable at `http://127.0.0.1:<vault_server_port>`.

Role Variables
--------------

`vault_server_install_path`: directory the Vault binary is installed into, default `/usr/local/bin/`.

`vault_server_binary_path`: path to the `vault` binary, default `/bin/vault`.

`vault_server_port`: port the local Vault server is listening on.

`vault_server_unseal_keys`: optional list of known unseal keys (e.g. captured from `vmutti.vault.server_db_create`).

Dependencies
------------

N/A

Example Playbook
-----------------

    - hosts: vault_server
      vars:
        vault_server_port: 8200
        vault_server_unseal_keys: "{{ vault_server_unseal_keys }}"
      roles:
         - role: vmutti.vault.server_db_unseal

License
-------

MIT

Author Information
------------------

Shoshana Makinen, [blog.vmutti.com](https://blog.vmutti.com)
