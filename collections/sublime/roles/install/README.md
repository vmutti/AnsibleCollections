vmutti.sublime.install
======================

Adds the Sublime Text apt repository and GPG key, installs the `sublime-text` package, and restores each configured user's saved Sublime configuration. Also exposes a `fetch_configs.yml` hook so `vmutti.configs.fetch` can back up this configuration.

Requirements
------------

Debian-based distro with apt. The target host must be a member of the `host_install_sublime` group.

Role Variables
--------------

`sublime_usernames`: list of usernames to restore Sublime configuration for.

`controller_sublime_config_dir` or `controller_tools_config_dir`: directory on the controller holding the backed-up Sublime user configuration.

Dependencies
------------

N/A

Example Playbook
-----------------

    - hosts: host_install_sublime
      vars:
        controller_tools_config_dir: '~/worchestation_configs/'
        sublime_usernames:
          - ansible
      roles:
         - role: vmutti.sublime.install

License
-------

MIT

Author Information
------------------

Shoshana Makinen, [blog.vmutti.com](https://blog.vmutti.com)
