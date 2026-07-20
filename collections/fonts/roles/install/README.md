vmutti.fonts.install
====================

Downloads each font archive listed in `font_urls`, extracts it into `~/.fonts/` for every user in `font_usernames`, and refreshes the font cache with `fc-cache`.

Requirements
------------

The target host must be a member of the `host_install_fonts` group.

Role Variables
--------------

`font_urls`: list of font archive URLs to download and install.

`font_usernames`: list of usernames to install fonts for.

Dependencies
------------

N/A

Example Playbook
-----------------

    - hosts: host_install_fonts
      vars:
        font_urls:
          - https://example.com/my-font.zip
        font_usernames:
          - ansible
      roles:
         - role: vmutti.fonts.install

License
-------

MIT

Author Information
------------------

Shoshana Makinen, [blog.vmutti.com](https://blog.vmutti.com)
