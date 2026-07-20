# vmutti.users

Creates and configures local user accounts on workstation hosts: human user accounts with sudo access, and VirtualBox shared-folder (`vboxsf`) group membership.

## Roles

- [common](roles/common/README.md) — shared feature-flag defaults consumed by the humans and virtualbox_shared_folders roles
- [humans](roles/humans/README.md) — creates human user accounts with sudo access
- [virtualbox_shared_folders](roles/virtualbox_shared_folders/README.md) — adds users to the vboxsf group for VirtualBox shared folder access

## License

MIT
