vmutti.gcloud.install
=====================

Adds Google Cloud's official apt repository and GPG key, then installs the `google-cloud-sdk` package.

Requirements
------------

Debian-based distro with apt. The target host must be a member of the `host_install_gcloud` group.

Role Variables
--------------

This role has no configurable variables.

Dependencies
------------

N/A

Example Playbook
-----------------

    - hosts: host_install_gcloud
      roles:
         - role: vmutti.gcloud.install

License
-------

MIT

Author Information
------------------

Shoshana Makinen, [blog.vmutti.com](https://blog.vmutti.com)
