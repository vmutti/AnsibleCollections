# vmutti.podman

Manages [Podman](https://podman.io) containers (create/start/stop) for hosts in a target inventory group, driven by per-host `podman_*` host variables, using the `containers.podman` collection.

## Roles

- [manage_containers](roles/manage_containers/README.md) — starts/stops a Podman container per guest host using its podman_* host variables

## License

MIT
