vmutti.libvirt.destroy
=======================

Deletes libvirt guest domains from a hypervisor. Unlike `vmutti.libvirt.deploy`, which builds its guest list from inventory, this role asks the hypervisor itself (via `community.libvirt.virt`'s `list_vms` command) which domains are actually defined, then deletes whichever of those match a regex — so it can clean up guests that have already been removed from inventory, not just ones still declared there.

Requirements
------------

`community.libvirt` (and its requirements, `python3-libvirt` and `python3-lxml`) must be installed on the hypervisor host. Run on a host acting as a libvirt hypervisor — see `vmutti.libvirt.install`.

Role Variables
--------------

`libvirt_uri`: libvirt connection URI, default `qemu:///system`.

`libvirt_destroy_pattern`: **required**, no default. A regex tested against every guest domain name defined on the hypervisor (via Ansible's `match` filter, so it anchors at the start of the name — write `.*` where needed, e.g. `^test-.*$` or just `^test-`). The role fails immediately if this is left blank, since an empty pattern would otherwise match everything.

`libvirt_destroy_confirm`: must be explicitly set `true` to run — the role fails immediately otherwise. This is a deliberate second guard on top of `libvirt_destroy_pattern`, since this role permanently deletes guest domains.

`libvirt_destroy_remove_storage`: default `false`. When `true`, passes the `delete_volumes` undefine flag so libvirt also deletes each matched domain's `file`-backed disk sources (its `disk_path`/`cdrom_path`). Leave `false` to undefine domains only and keep their disk images on the hypervisor.

Note this flag never touches pool-backed volumes — anything a guest attached via `libvirt_volumes` in `vmutti.libvirt.deploy` (see that role's README) is a `<disk type="volume">`, not `type="file"`, so it's structurally exempt and always survives the domain being undefined, regardless of this setting. Delete those explicitly with `virt_volume` if you actually want them gone.

What it does
------------

1. Fails if `libvirt_destroy_pattern` is empty or `libvirt_destroy_confirm` isn't `true`.
2. Lists every guest domain currently defined on the hypervisor and filters it against `libvirt_destroy_pattern`.
3. Force-powers-off each matched domain (`state: destroyed`; a no-op if it's already shut down).
4. Undefines each matched domain, with the `delete_volumes` flag when `libvirt_destroy_remove_storage` is `true`.

Dependencies
------------

`community.libvirt`

Example Playbook
-----------------

    - hosts: "{{ target_hosts | default('all') }}:&libvirt_hypervisor"
      roles:
        - vmutti.libvirt.destroy

Always pass the pattern and confirmation on the command line rather than hardcoding them, and scope `target_hosts`/`--limit` to the hypervisor(s) you actually mean:

    ansible-playbook vmutti.libvirt.destroy \
      -e target_hosts=dev.Thiala.local.vmutti.com \
      -e libvirt_destroy_pattern='^test-' \
      -e libvirt_destroy_confirm=true \
      -e libvirt_destroy_remove_storage=true

License
-------

MIT

Author Information
------------------

Shoshana Makinen, [blog.vmutti.com](https://blog.vmutti.com)
