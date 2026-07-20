vmutti.vault.server_tls_disable
===============================

Writes a Vault config with TLS disabled (file storage, plaintext listener on `127.0.0.1:8200`) to the hypervisor's Vault config directory, then stops and restarts the Vault server (via the role named in `vault_server_manage_role`) to pick it up. Intended as a temporary state during initial setup, before real TLS certificates are available.

Requirements
------------

A `vault_server_manage_role` capable of stopping/starting the server (e.g. `vmutti.vault.podman_server_manage`).

Role Variables
--------------

`vault_tls_disabled_config`: the Vault HCL-as-JSON config written out; defaults to file storage with TLS disabled on `127.0.0.1:8200`.

`vault_hypervisor_config_path`: directory on the hypervisor to write `vault.json` into.

`vault_server_manage_role`: fully-qualified role name used to stop/start the Vault server.

Dependencies
------------

N/A

Example Playbook
-----------------

    - hosts: vault_hypervisor
      vars:
        vault_server_manage_role: vmutti.vault.podman_server_manage
      roles:
         - role: vmutti.vault.server_tls_disable

License
-------

MIT

Author Information
------------------

Shoshana Makinen, [blog.vmutti.com](https://blog.vmutti.com)
