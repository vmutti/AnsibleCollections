vmutti.kubectl.install
======================

Adds the Kubernetes apt GPG key and repository for the configured release channel, then installs the `kubectl` package.

Requirements
------------

Debian-based distro with apt. The target host must be a member of the `host_install_kubectl` group.

Role Variables
--------------

`kubectl_version`: Kubernetes release channel to track (used to build the pkgs.k8s.io repo URL), default `v1.35`.

Dependencies
------------

N/A

Example Playbook
-----------------

    - hosts: host_install_kubectl
      roles:
         - role: vmutti.kubectl.install

License
-------

MIT

Author Information
------------------

Shoshana Makinen, [blog.vmutti.com](https://blog.vmutti.com)
