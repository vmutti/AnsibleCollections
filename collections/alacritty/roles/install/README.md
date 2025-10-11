vmutti.alacritty.install
=========

Installs [Alacritty](https://github.com/alacritty/alacritty) and configures it. Also provides a list of files to fetch when backing up configurations using `vmutti.configs.fetch`.
 

Requirements
------------

Right now, this role only works for debian-based distros and has only been tested with XFCE.
The target host must be part of the `host_install_alacritty` group.

Role Variables
--------------

`alacritty_user_config_paths`:See `vmutti.config.fetch` for details on the format of this variable. It represents the files in the user's home directory to fetch when backing up configurations. This is set automatically to the following value that works for the author's configuration:
  - {path: ".config/", recurse: false}
  - .config/alacritty

`controller_alacritty_config_dir` or `controller_tools_config_dir`: Either the directory on the controller holding the alacritty user configuration or the controller directory that has an `alacritty` subdirectory containing these configurations respectively.


Dependencies
------------

N/A

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

MIT

Author Information
------------------

[Website](https://blog.vmutti.com)