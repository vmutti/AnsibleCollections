vmutti.worchestation.provision
==============================

Meta-role that includes ~20 other `vmutti.*` roles (updates, VirtualBox guest additions, human user setup, zsh/tmux/vim/wireguard, XFCE/fonts/chrome/alacritty/sublime, docker/gcloud/kubectl/kind, golang, and security tools like autochrome/mitmproxy/burp/kali) behind tags such as `base`, `gui`, `tools`, and `virtualbox_guest`, so a host's group membership decides which subset actually runs.

Requirements
------------

Each included role has its own requirements (see that role's README). Typically driven by inventory groups named `host_install_$TOOL`.

Role Variables
--------------

No variables of its own beyond `--tags`/`--skip-tags` selection; see the individual included roles for their variables.

Dependencies
------------

vmutti.updates, vmutti.virtualbox_guest, vmutti.users, vmutti.zsh, vmutti.tmux, vmutti.vim, vmutti.wireguard, vmutti.xfce, vmutti.fonts, vmutti.chrome, vmutti.alacritty, vmutti.sublime, vmutti.docker, vmutti.gcloud, vmutti.kubectl, vmutti.kind, vmutti.golang, vmutti.autochrome, vmutti.mitmproxy, vmutti.burp, vmutti.kali

Example Playbook
-----------------

    - hosts: worchestation
      roles:
         - role: vmutti.worchestation.provision

License
-------

MIT

Author Information
------------------

Shoshana Makinen, [blog.vmutti.com](https://blog.vmutti.com)
