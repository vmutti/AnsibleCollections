vmutti.podman.manage_containers
===============================

For each host in the target guest group, manages a Podman container using that host's `podman_image`, `podman_command`, `podman_volumes`, `podman_env`, `podman_cap_add`, and related `podman_*` host variables via the `containers.podman.podman_container` module. Optionally installs a Python interpreter into Alpine-based containers so Ansible can manage them directly.

Requirements
------------

The `containers.podman` collection must be installed on the controller/target. Podman must be installed on the host running the containers.

Role Variables
--------------

`podman_guest_group` / `vagrant_guest_group`: inventory group whose hosts' `podman_*` variables describe the containers to manage.

`podman_containers_state`: desired state passed to `podman_container` (e.g. `started`, `stopped`, `absent`).

Per-guest host variables: `podman_image`, `podman_command`, `podman_volumes`, `podman_env`, `podman_cap_add`, `podman_hostuser`, `podman_userns`, `podman_uidmap`, `podman_gidmap`, `podman_alpine_python_install`.

Dependencies
------------

containers.podman

Example Playbook
-----------------

    - hosts: podman_hypervisor
      vars:
        podman_guest_group: my_podman_guests
      roles:
         - role: vmutti.podman.manage_containers

License
-------

MIT

Author Information
------------------

Shoshana Makinen, [blog.vmutti.com](https://blog.vmutti.com)
