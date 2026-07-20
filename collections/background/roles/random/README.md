vmutti.background.random
========================

Downloads a random 1920x1200 image from [picsum.photos](https://picsum.photos) and overwrites the system default desktop background with it.

Requirements
------------

The target host must be a member of the `host_install_background` group.

Role Variables
--------------

`random_background_force`: boolean, default `false`. Must be set to `true` for the background to actually be downloaded and replaced.

Dependencies
------------

N/A

Example Playbook
-----------------

    - hosts: host_install_background
      vars:
        random_background_force: true
      roles:
         - role: vmutti.background.random

License
-------

MIT

Author Information
------------------

Shoshana Makinen, [blog.vmutti.com](https://blog.vmutti.com)
