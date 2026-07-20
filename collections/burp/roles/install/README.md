vmutti.burp.install
===================

Downloads the Burp Suite Professional installer for a pinned version and silently installs it for each configured user, then restores that user's saved Burp configuration. Also exposes a `fetch_configs.yml` hook so `vmutti.configs.fetch` can back up this configuration.

Requirements
------------

The target host must be a member of the `host_install_burp` group. A valid Burp Suite Pro license/activation is required after install.

Role Variables
--------------

`burp_version`: Burp Suite Pro version to download, default `2024.11.2`.

`burp_usernames`: list of usernames to install Burp for.

`controller_burp_config_dir` or `controller_tools_config_dir`: directory on the controller holding the backed-up Burp user configuration.

Dependencies
------------

N/A

Example Playbook
-----------------

    - hosts: host_install_burp
      vars:
        controller_tools_config_dir: '~/worchestation_configs/'
        burp_usernames:
          - ansible
      roles:
         - role: vmutti.burp.install

License
-------

MIT

Author Information
------------------

Shoshana Makinen, [blog.vmutti.com](https://blog.vmutti.com)
