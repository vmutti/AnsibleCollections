# vmutti.vagrant

Generates a Vagrant project directory (guest configuration derived from inventory hosts in a guest group) on a hypervisor host, and runs `vagrant up` to bring the guests online. Guests are read from Ansible inventory (see `vmutti.vagrant.AnsibleVagrantConfigurer`-style `Vagrantfile` integration) rather than being hand-written.

## Roles

- [deploy](roles/deploy/README.md) — writes the Vagrant project/guest configs and runs vagrant up for each guest

## License

MIT
