# vmutti.packer

Builds [Packer](https://www.packer.io) machine images for guest hosts defined in a Packer/Vagrant hypervisor group. For each guest, composes builder/provisioner/post-processor JSON configuration from default, platform, distro, packager, and profile fragments read from `controller_packer_config_dir`, writes it out, and kicks off an asynchronous `packer build`.

## Roles

- [build](roles/build/README.md) — renders per-guest Packer configs and runs packer build for each one

## Playbooks

- `playbooks/build.yml`: runs `vmutti.packer.build` against the `vagrant_hypervisor` group.

## License

MIT
