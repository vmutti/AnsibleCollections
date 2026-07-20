vmutti.users.virtualbox_shared_folders
======================================

Adds each username in `virtualbox_sf_usernames` to the `vboxsf` group so they can access VirtualBox shared folders, when `host_setup_virtualbox_users` is true.

Requirements
------------

VirtualBox Guest Additions must already be installed (see `vmutti.virtualbox_guest.install`) so the `vboxsf` group exists.

Role Variables
--------------

`host_setup_virtualbox_users`: boolean. Must be true for group membership to be applied (see `vmutti.users.common`).

`virtualbox_sf_usernames`: list of usernames to add to the `vboxsf` group.

Dependencies
------------

N/A

Example Playbook
-----------------

    - hosts: all
      vars:
        host_setup_virtualbox_users: true
        virtualbox_sf_usernames:
          - ansible
      roles:
         - role: vmutti.users.virtualbox_shared_folders

License
-------

MIT

Author Information
------------------

Shoshana Makinen, [blog.vmutti.com](https://blog.vmutti.com)
