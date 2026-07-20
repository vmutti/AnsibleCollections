vmutti.tmux.install
===================

Installs `tmux` and restores each configured user's saved tmux configuration. Also exposes a `fetch_configs.yml` hook so `vmutti.configs.fetch` can back up this configuration.

Requirements
------------

Debian-based distro with apt. The target host must be a member of the `host_install_tmux` group.

Role Variables
--------------

`tmux_usernames`: list of usernames to restore tmux configuration for, defaults to `[main_username]`.

`controller_tmux_config_dir` or `controller_tools_config_dir`: directory on the controller holding the backed-up tmux user configuration.

Dependencies
------------

N/A

Example Playbook
-----------------

    - hosts: host_install_tmux
      vars:
        controller_tools_config_dir: '~/worchestation_configs/'
      roles:
         - role: vmutti.tmux.install

License
-------

MIT

Author Information
------------------

Shoshana Makinen, [blog.vmutti.com](https://blog.vmutti.com)
