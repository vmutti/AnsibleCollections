# vmutti.virtualbox_guest

Installs VirtualBox Guest Additions inside a VM, with distro-specific installation steps (currently Debian and Kali). Commonly used as a provisioner during a `vmutti.packer.build` image build.

## Roles

- [install](roles/install/README.md) — installs VirtualBox Guest Additions using the appropriate distro-specific task file

## License

MIT
