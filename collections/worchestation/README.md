# vmutti.worchestation

Worchestation (pronounced "Wuss-station") is a tool used to orchestrate personal workstations. It bundles a curated set of `vmutti.*` roles — base shell/editor/terminal tools, a GUI desktop environment, and development/security tooling — behind Ansible tags, so a host's inventory group membership (`host_install_$TOOL` groups) determines which tool set it receives. This lets a headless WSL host get just the terminal/dev tools while a full VM gets the GUI apps too.

## Roles

- [provision](roles/provision/README.md) — includes the full set of vmutti.* roles behind tags to provision a workstation, including `vmutti.storage.mount` for disk drives

## Building a disk image

Use an existing box, or use the [PackerImages](https://github.com/vmutti/PackerImages) build scripts to make your own with Worchestation already applied.

## Setting up a VM

Use the configuration instructions at [vmutti.vagrant](https://galaxy.ansible.com/ui/repo/published/vmutti/vagrant/) to configure your inventory, then use `vmutti.vagrant.deploy` to deploy and provision the Vagrant machines.

## Provisioning

Configure your inventory with groups named `host_install_$TOOL` for each tool you want installed. Ensure any variables required by the roles Worchestation depends on are set.

## License

MIT
