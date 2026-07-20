vmutti.docker.install
=====================

Adds Docker's official apt repository, installs `docker-ce`, `docker-ce-cli`, and `containerd.io`, installs the `docker-compose` CLI plugin, and adds each configured user to the `docker` group.

Requirements
------------

Debian-based distro with apt (bookworm, or kali-rolling treated as bookworm). The target host must be a member of the `host_install_docker` group.

Role Variables
--------------

`docker_compose_version`: version of the docker-compose CLI plugin to install, default `v5.0.1`.

`docker_cli_plugins_dir`: directory to install the docker-compose CLI plugin binary into, default `/usr/libexec/docker/cli-plugins`.

`docker_usernames`: list of usernames to add to the `docker` group.

Dependencies
------------

N/A

Example Playbook
-----------------

    - hosts: host_install_docker
      vars:
        docker_usernames:
          - ansible
      roles:
         - role: vmutti.docker.install

License
-------

MIT

Author Information
------------------

Shoshana Makinen, [blog.vmutti.com](https://blog.vmutti.com)
