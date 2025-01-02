# Worchestation

Worchestation(Pronounced Wuss-station) is a tool that I use to orchestrate my personal workstations.
It essentially just bundles a bunch of my roles that install and configure my workstation repeatably.
This way I can use my inventory to specify that my machine running WSL is a headless workstation and have all of my terminal and development tools installed without the gui apps.  Then I can do a full install of the tools I need for a particular project in its VM. 
I also have tools for managing these configurations once you tweak them and for setting up these VMs based on hosts configured in the Inventory

## Building a disk image

You can use an existing box or use my [build scripts](https://github.com/vmutti/PackerImages) to make your own with Worchestation already applied.

## Setting up a VM

Use the configuration instructions at [vmutti.vagrant](https://galaxy.ansible.com/ui/repo/published/vmutti/vagrant/) to configure your inventory and then use `vmutti.worchestation.deploy` to deploy the vagrant machines and provision them.

## Provisioning

Configure your inventory with groups named `host_install_$TOOL` where `$TOOL` is the tool that you intend to install. Ensure that any of the roles that worchestation depends on have the proper variables set.
