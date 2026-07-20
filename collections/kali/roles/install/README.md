vmutti.kali.install
===================

Installs the Kali archive keyring, adds the Kali apt repository (`kali-last-snapshot`), and installs the packages listed in `kali_packages` (e.g. `nmap`, `burpsuite`, `metasploit-framework`, `wireshark`).

Requirements
------------

Debian-based distro with apt. The target host must be a member of the `host_install_kali` group.

Role Variables
--------------

`kali_version`: Kali release used to fetch the archive-keyring package, default `2025.2`.

`kali_packages`: list of Kali packages to install. Empty by default.

Dependencies
------------

N/A

Example Playbook
-----------------

    - hosts: host_install_kali
      vars:
        kali_packages:
          - nmap
          - burpsuite
          - wireshark
      roles:
         - role: vmutti.kali.install

License
-------

MIT

Author Information
------------------

Shoshana Makinen, [blog.vmutti.com](https://blog.vmutti.com)
