vmutti.configs.fetch
====================

For each entry in `fetch_services`, optionally includes that service's own role-provided `fetch_configs.yml` (to collect its default config paths), then tars/gzips the resulting user and system paths on the target host and fetches the archives back to the controller as `user.tar.gz`/`system.tar.gz`. This is the backup half of the config restore performed by roles like `vmutti.alacritty.install`, `vmutti.tmux.install`, `vmutti.vim.install`, `vmutti.xfce.install`, and `vmutti.zsh.install`.

Requirements
------------

`tar` must be available on the target host. Run with enough privilege (`become: true`) to read the paths being archived.

Role Variables
--------------

`fetch_services`: list of service definitions. Each entry supports `name` (required), `role` (an optional role providing a `fetch_configs.yml` hook), `username` (defaults to `fetch_default_username`), `controller_config_dir` (defaults to `<fetch_default_controller_config_dir>/<name>`), `user_paths`, and `system_paths`.

`fetch_default_username`: default username whose home directory user paths are relative to. Defaults to `main_username`.

`fetch_default_controller_config_dir`: default base directory on the controller to write fetched archives under. Defaults to `<controller_tools_config_dir>_fetched`.

Dependencies
------------

N/A

Example Playbook
-----------------

    - hosts: worchestation
      vars:
        fetch_services:
          - name: vim
            role: vmutti.vim.install
      roles:
         - role: vmutti.configs.fetch

License
-------

MIT

Author Information
------------------

Shoshana Makinen, [blog.vmutti.com](https://blog.vmutti.com)
