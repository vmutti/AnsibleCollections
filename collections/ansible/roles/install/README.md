vmutti.ansible.install
======================

Installs the `ansible` Python package via `pip` so the target host can itself run Ansible (for example, a workstation that needs to manage other hosts).

Requirements
------------

None beyond a working `pip` on the target host.

Role Variables
--------------

`host_install_ansible`: boolean. When true, installs the `ansible` pip package.

Dependencies
------------

N/A

Example Playbook
-----------------

    - hosts: host_install_ansible
      vars:
        host_install_ansible: true
      roles:
         - role: vmutti.ansible.install

License
-------

MIT

Author Information
------------------

Shoshana Makinen, [blog.vmutti.com](https://blog.vmutti.com)
