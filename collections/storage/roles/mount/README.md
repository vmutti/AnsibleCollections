vmutti.storage.mount
=====================

Formats (if needed) and mounts a host's configured disk drives on boot. Works the same way whether the host is a libvirt hypervisor mounting its own physical disks, or a libvirt guest mounting a data volume libvirt attached to it — it's just a list of `disk_mounts`, driven entirely by inventory.

Requirements
------------

Debian-based distro. Uses `community.general.filesystem` and `ansible.posix.mount`.

Role Variables
--------------

`disk_mounts`: a list of drives to mount, default `[]`. Each entry:

    disk_mounts:
      - mount_point: /var/lib/libvirt/pools/storage
        device: /dev/sda
        fstype: ext4
      - mount_point: /mnt/storage
        label: example-storage
        fstype: ext4

Keys: `mount_point` (required), and at least one of `device` (a raw block device path, e.g. a hypervisor's own physical disk like `/dev/sda`) or `label` (a filesystem label, e.g. a libvirt-attached guest volume that was labeled when its filesystem was created — see `vmutti.libvirt.deploy`'s `libvirt_volumes`). `fstype` (default `ext4`), `opts` (mount options, default `defaults`), `owner`/`group`/`mode` for the mount point directory (defaults `root`/`root`/`0755`), `create_filesystem` (default `true` — set `false` to skip filesystem creation and only mount an already-formatted drive).

When both `device` and `label` are set, the role formats `device` (passing `-L <label>` to `mkfs`) but then mounts by `LABEL=<label>` rather than the device path, so the mount keeps working even if the kernel enumerates attached disks in a different order across reboots (common for libvirt guests, where `/dev/vdb` isn't guaranteed to stay `/dev/vdb`). Filesystem creation is idempotent — it's skipped if the device already has a filesystem, so it's safe to leave `create_filesystem: true` on every run.

What it does
------------

For each entry in `disk_mounts`:

1. Creates a filesystem on `device` (skipped if one already exists, or if only `label` is set).
2. Ensures `mount_point` exists.
3. Adds an `/etc/fstab` entry and mounts it (`ansible.posix.mount`, `state: mounted`), preferring `LABEL=` over the raw device path when a label is set.

Dependencies
------------

N/A

Example Playbook
-----------------

    - hosts: all
      roles:
         - role: vmutti.storage.mount

License
-------

MIT

Author Information
------------------

Shoshana Makinen, [blog.vmutti.com](https://blog.vmutti.com)
