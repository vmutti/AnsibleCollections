vmutti.zsh.install
==================

Installs `zsh`, `git`, and (on Debian) `fonts-powerline`, clones Oh My Zsh, and for each configured user: installs Oh My Zsh, restores their saved `.zshrc` configuration, and sets `zsh` as their login shell. Also exposes a `fetch_configs.yml` hook so `vmutti.configs.fetch` can back up this configuration.

Requirements
------------

Debian-based distro with apt. The target host must be a member of the `host_install_zsh` group.

Role Variables
--------------

`zsh_usernames`: list of usernames to configure zsh for, defaults to `[main_username]`.

`controller_zsh_config_dir` or `controller_tools_config_dir`: directory on the controller holding the backed-up `.zshrc`.

Dependencies
------------

N/A

Example Playbook
-----------------

    - hosts: host_install_zsh
      vars:
        controller_tools_config_dir: '~/worchestation_configs/'
      roles:
         - role: vmutti.zsh.install

License
-------

MIT

Author Information
------------------

Shoshana Makinen, [blog.vmutti.com](https://blog.vmutti.com)
