vmutti.autochrome.install
=========================

Installs `git`/`ruby`, clones [NCC Group's Autochrome](https://github.com/nccgroup/autochrome), and runs it for each configured user to harden their Chrome/Chromium extension security settings.

Requirements
------------

Debian-based distro with apt. The target host must be a member of the `host_install_autochrome` group.

Role Variables
--------------

`autochrome_usernames`: list of usernames to run Autochrome for.

Dependencies
------------

N/A

Example Playbook
-----------------

    - hosts: host_install_autochrome
      vars:
        autochrome_usernames:
          - ansible
      roles:
         - role: vmutti.autochrome.install

License
-------

MIT

Author Information
------------------

Shoshana Makinen, [blog.vmutti.com](https://blog.vmutti.com)
