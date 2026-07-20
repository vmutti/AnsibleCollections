vmutti.vault.podman_server_manage
=================================

Ensures the Vault storage directory exists with the correct permissions, then delegates to `vmutti.podman.manage_containers` to start or stop the Vault server's Podman container.

Requirements
------------

`vmutti.podman` must be installed. Podman must be available on the target host.

Role Variables
--------------

`vault_hypervisor_storage_path`: path to the Vault storage directory to create.

`vault_server_state`: desired container state (e.g. `started`/`stopped`), passed through as `podman_containers_state`.

`vault_server_guest_name`: guest host name identifying the Vault container, passed through as `podman_guest_name`.

Dependencies
------------

vmutti.podman

Example Playbook
-----------------

    - hosts: vault_hypervisor
      vars:
        vault_server_state: started
        vault_server_guest_name: vault01
      roles:
         - role: vmutti.vault.podman_server_manage

License
-------

MIT

Author Information
------------------

Shoshana Makinen, [blog.vmutti.com](https://blog.vmutti.com)
