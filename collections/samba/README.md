# vmutti.samba

Not yet wrapped as an Ansible role: `install.sh` installs Samba, and if `~/configs/samba/config.tar.gz` exists, restores it (including any backed-up `smb.conf` and `users.backup.tdb` password database).

## Usage

Run `install.sh` on the target host (for example, via Ansible's `script` module) as a user that can `sudo`.

## License

MIT
