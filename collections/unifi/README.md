# vmutti.unifi

Not yet wrapped as an Ansible role: `install.sh` installs Java and other dependencies, adds Ubiquiti's apt repository, installs the UniFi Network Controller, and copies a dedicated network interface config from `~/configs/unifi/60-unifieth.cfg`.

## Usage

Run `install.sh` on the target host (for example, via Ansible's `script` module) as a user that can `sudo`.

## License

MIT
