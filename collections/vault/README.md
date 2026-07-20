# vmutti.vault

Deploys and manages a [HashiCorp Vault](https://www.vaultproject.io) server running in a Podman container: starting/stopping the container, initializing and unsealing the Vault database, temporarily disabling TLS during setup, destroying its storage, and running arbitrary `vault` CLI commands.

## Roles

- [common](roles/common/README.md) — shared defaults for the other vault roles
- [podman_server_manage](roles/podman_server_manage/README.md) — starts/stops the Vault server's Podman container
- [server_db_create](roles/server_db_create/README.md) — initializes a new Vault database, capturing the root token and unseal keys
- [server_db_destroy](roles/server_db_destroy/README.md) — stops the Vault server and deletes its storage directory
- [server_db_init](roles/server_db_init/README.md) — runs a Vault command against the server as part of initial setup
- [server_db_unseal](roles/server_db_unseal/README.md) — unseals the Vault server using known or interactively-provided unseal keys
- [server_tls_disable](roles/server_tls_disable/README.md) — writes a TLS-disabled Vault config and restarts the server for initial bootstrap
- [server_vault_command](roles/server_vault_command/README.md) — runs an arbitrary vault CLI command with a given address/token

## Playbooks

- `playbooks/server_provision_test.yml`: an example end-to-end bootstrap/provision flow across the `vault_hypervisor` and `vault_server` groups. Note it references a few roles (`server_db_deploy_admin_user`, `server_db_deploy_root_ca`, `server_db_deploy_int_ca`) that don't exist in this collection yet.

## Note

This collection is under active development: some roles reference host variables (`vault_hypervisor_storage_path`, `vault_hypervisor_config_path`, `vault_server_manage_role`, `vault_server_guest_name`, `vault_server_port`) that are expected to be supplied by the consuming inventory rather than defaulted here.

## License

MIT
