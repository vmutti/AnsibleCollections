vmutti.mitmproxy.install
========================

Downloads the mitmproxy release tarball for the host's architecture and extracts it into `mitmproxy_install_dir`.

Requirements
------------

The target host must be a member of the `host_install_mitmproxy` group.

Role Variables
--------------

`mitmproxy_version`: mitmproxy release to install, default `11.0.1`.

`mitmproxy_install_dir`: directory to extract the binaries into, default `/usr/local/bin`.

Dependencies
------------

N/A

Example Playbook
-----------------

    - hosts: host_install_mitmproxy
      roles:
         - role: vmutti.mitmproxy.install

License
-------

MIT

Author Information
------------------

Shoshana Makinen, [blog.vmutti.com](https://blog.vmutti.com)
