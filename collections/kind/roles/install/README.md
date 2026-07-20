vmutti.kind.install
===================

Downloads the `kind` CLI binary for the host's OS/architecture and installs it to `/usr/local/bin/kind`.

Requirements
------------

The target host must be a member of the `host_install_kind` group.

Role Variables
--------------

`kind_version`: kind release to install, default `0.25.0`.

`kind_install_dir`: directory to install the binary into, default `/usr/local/bin`.

Dependencies
------------

N/A

Example Playbook
-----------------

    - hosts: host_install_kind
      roles:
         - role: vmutti.kind.install

License
-------

MIT

Author Information
------------------

Shoshana Makinen, [blog.vmutti.com](https://blog.vmutti.com)
