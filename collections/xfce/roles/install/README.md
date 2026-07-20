vmutti.xfce.install
===================

Installs the `xfce4` and `thunar-archive-plugin` packages, restores a system-level configuration archive to `/`, and restores each configured user's saved XFCE configuration. Also exposes a `fetch_configs.yml` hook so `vmutti.configs.fetch` can back up this configuration.

Requirements
------------

Debian-based distro with apt. The target host must be a member of the `host_install_xfce` group.

Role Variables
--------------

`xfce_usernames`: list of usernames to restore XFCE configuration for.

`controller_xfce_config_dir` or `controller_tools_config_dir`: directory on the controller holding the backed-up XFCE system/user configuration.

Dependencies
------------

N/A

Example Playbook
-----------------

    - hosts: host_install_xfce
      vars:
        controller_tools_config_dir: '~/worchestation_configs/'
        xfce_usernames:
          - ansible
      roles:
         - role: vmutti.xfce.install

License
-------

MIT

Author Information
------------------

Shoshana Makinen, [blog.vmutti.com](https://blog.vmutti.com)
