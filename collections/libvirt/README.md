# vmutti.libvirt

Installs [libvirt](https://libvirt.org)/QEMU-KVM and adds specified users to the `libvirt` and `kvm` groups, turning a host into a hypervisor capable of running VMs (e.g. via the `vagrant-libvirt` provider). Also deploys libvirt storage pools, networks, and guest domains on that hypervisor from inventory, using the `community.libvirt` collection.

## Roles

- [install](roles/install/README.md) — installs libvirt/QEMU-KVM packages, enables libvirtd, and configures user group membership
- [deploy](roles/deploy/README.md) — defines libvirt storage pools and networks from hypervisor variables, and guest domains from a `libvirt_guests` inventory group
- [destroy](roles/destroy/README.md) — deletes guest domains (and optionally their disks) from a hypervisor by matching their names against a regex

## Playbooks

- `playbooks/deploy.yml` — runs the `deploy` role against `libvirt_hypervisor` hosts (optionally scoped with `-e target_hosts=<hostname>`)
- `playbooks/destroy.yml` — runs the `destroy` role against `libvirt_hypervisor` hosts; requires `-e libvirt_destroy_pattern=<regex> -e libvirt_destroy_confirm=true`

## License

MIT
