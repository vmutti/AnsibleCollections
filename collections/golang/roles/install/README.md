vmutti.golang.install
=====================

Downloads the Go toolchain archive for the host's architecture, extracts it into `golang_install_dir`, and appends the Go/GOPATH `bin` directories to each configured user's `PATH` via their `.zshrc`.

Requirements
------------

The target host must be a member of the `host_install_golang` group. Assumes users have a `.zshrc` (see `vmutti.zsh.install`).

Role Variables
--------------

`golang_version`: Go version to install, default `1.25.5`.

`golang_install_dir`: directory to extract the Go toolchain into, default `/usr/local`.

`golang_usernames`: list of usernames whose `.zshrc` PATH should be updated.

Dependencies
------------

N/A

Example Playbook
-----------------

    - hosts: host_install_golang
      vars:
        golang_usernames:
          - ansible
      roles:
         - role: vmutti.golang.install

License
-------

MIT

Author Information
------------------

Shoshana Makinen, [blog.vmutti.com](https://blog.vmutti.com)
