vmutti.vim.install
==================

Installs `vim` and `git`, then for each configured user restores their saved vim configuration (`.vimrc`, `.vim_runtime/`). Also exposes a `fetch_configs.yml` hook so `vmutti.configs.fetch` can back up this configuration.

Requirements
------------

Debian-based distro with apt. The target host must be a member of the `host_install_vim` group.

Role Variables
--------------

`vim_usernames`: list of usernames to restore vim configuration for.

`controller_vim_config_dir` or `controller_tools_config_dir`: directory on the controller holding the backed-up vim user configuration.

Dependencies
------------

N/A

Example Playbook
-----------------

    - hosts: host_install_vim
      vars:
        controller_tools_config_dir: '~/worchestation_configs/'
        vim_usernames:
          - ansible
      roles:
         - role: vmutti.vim.install

License
-------

MIT

Author Information
------------------

Shoshana Makinen, [blog.vmutti.com](https://blog.vmutti.com)
