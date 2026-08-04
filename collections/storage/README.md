# vmutti.storage

Formats and mounts a host's disk drives, by device path or filesystem label. Used for both a libvirt hypervisor's own physical disks and a libvirt guest's attached data volumes — see `vmutti.libvirt`.

## Roles

- [mount](roles/mount/README.md) — formats (if needed) and mounts a host's configured `disk_mounts` on boot

## License

MIT
