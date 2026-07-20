vmutti.wireguard.install
========================

Installs the `wireguard` and `resolvconf` packages, and if a backed-up `system.tar.gz` exists under `controller_wireguard_config_dir`, extracts it to `/` to restore WireGuard's system configuration. Also exposes a `fetch_configs.yml` hook so `vmutti.configs.fetch` can back up this configuration.

Requirements
------------

Debian-based distro with apt. The target host must be a member of the `host_install_wireguard` group.

Role Variables
--------------

`controller_wireguard_config_dir` or `controller_tools_config_dir`: directory on the controller holding the backed-up WireGuard system configuration.

Dependencies
------------

N/A

Example Playbook
-----------------

    - hosts: host_install_wireguard
      vars:
        controller_tools_config_dir: '~/worchestation_configs/'
      roles:
         - role: vmutti.wireguard.install

License
-------

MIT

Author Information
------------------

Shoshana Makinen, [blog.vmutti.com](https://blog.vmutti.com)
