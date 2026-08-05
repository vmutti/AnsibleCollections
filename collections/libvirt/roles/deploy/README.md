vmutti.libvirt.deploy
======================

Deploys libvirt storage pools, networks, and guest domains on a libvirt hypervisor host using the `community.libvirt` collection modules (`virt_pool`, `virt_net`, `virt`).

Pools and networks are generated from dictionary variables set on the hypervisor host itself. Guest domains are generated from inventory: any host in `libvirt_guest_group` whose `libvirt_hypervisor` variable identifies this hypervisor gets defined (and started) here, the same way `vmutti.vagrant.deploy` builds Vagrant guest configs from a guest group.

Requirements
------------

`community.libvirt` (and its requirements, `python3-libvirt` and `python3-lxml`) must be installed on the hypervisor host. Run on a host acting as a libvirt hypervisor — see `vmutti.libvirt.install` for installing libvirt/QEMU-KVM itself.

Role Variables
--------------

`libvirt_uri`: libvirt connection URI, default `qemu:///system`.

`libvirt_guest_group`: inventory group containing every libvirt guest across all hypervisors, default `libvirt_guests`.

`libvirt_hypervisor_identifier`: the value guests must set in their `libvirt_hypervisor` variable to be deployed onto this host, default `{{ inventory_hostname }}`.

`libvirt_guest_default_state`: state guest domains are put into when a guest doesn't set its own `libvirt_state`, default `running`.

`libvirt_enable_ip_forward`: whether to persist and apply `net.ipv4.ip_forward = 1` on the hypervisor when a routed network is defined, default `true`. See [Routing a network onto the LAN](#routing-a-network-onto-the-lan).

`libvirt_manage_apparmor_pools`: whether to grant libvirtd's AppArmor profile access to configured `libvirt_pool_*` target paths, default `true`. See [AppArmor and custom pool paths](#apparmor-and-custom-pool-paths).

### Pools and networks

Set on the hypervisor host (or a group it belongs to). Every hostvar matching `^libvirt_pool_.*$` becomes one storage pool; every hostvar matching `^libvirt_net_.*$` becomes one network. The variable name itself is arbitrary (only the prefix is matched) — use it to give each definition a distinct key.

    libvirt_pool_images:
      name: images
      type: dir
      target_path: /var/lib/libvirt/images/guests
      autostart: true

    libvirt_net_guests:
      name: guests
      forward_mode: nat
      bridge_name: virbr-guests
      domain_name: guests.local
      ip:
        address: 192.168.122.1
        netmask: 255.255.255.0
        dhcp_range:
          start: 192.168.122.10
          end: 192.168.122.200

Pool keys: `name` (required), `type` (default `dir`), `uuid`, `target_path`, `permissions.{owner,group,mode}`, `source.{host,dir,device,name,format}`, `autostart` (default `true`), `build` (default `true`, set `false` to skip the `virt_pool` build command for pool types that don't support/need it).

Network keys: `name` (required), `uuid`, `forward_mode` (omit for an isolated network), `forward_dev`, `bridge_name`, `stp`, `delay`, `domain_name`, `ip.{address,netmask}`, `ip.dhcp_range.{start,end}`, `ip.dhcp_hosts` (list of `{mac, name, ip}`), `autostart` (default `true`).

Guests that don't set their own `libvirt_network` fall back to libvirt's built-in `default` network, which the package defines but doesn't start or autostart. The role always ensures `default` is active and set to autostart, independent of any `libvirt_net_*` definitions.

### Routing a network onto the LAN

By default `forward_mode: nat` (or an omitted `forward_mode`, for an isolated network) hides guests behind the hypervisor's IP via masquerading — nothing upstream of the hypervisor can reach them directly. Set `forward_mode: route` instead to make libvirt treat the network as a plain routed subnet: guests keep their real IPs on the wire, libvirt adds `ACCEPT` forwarding rules (no masquerade) between the network's bridge and the rest of the host, and the subnet becomes reachable from the LAN once the LAN's router/gateway knows to send traffic for it to the hypervisor.

    libvirt_net_lan_routed:
      name: lan-routed
      forward_mode: route
      forward_dev: eth0
      bridge_name: virbr-lan
      domain_name: lan.local
      ip:
        address: 192.168.50.1
        netmask: 255.255.255.0
        dhcp_range:
          start: 192.168.50.10
          end: 192.168.50.200

`forward_dev` is optional and restricts libvirt's forwarding rules to a single host NIC (typically the one facing the LAN) instead of every interface on the box — set it to the hypervisor's LAN-facing interface name.

Pick a subnet (`ip.address`/`ip.netmask`) that doesn't overlap any existing LAN subnet or other libvirt network, since it needs its own routing entry upstream. The hypervisor's LAN IP becomes the next-hop gateway for that subnet — see your router/gateway's documentation for how to add a static route for it (e.g. a USG: `Settings > Networks > Create New Network`, type "Static Route", destination the guest subnet in CIDR, next hop the hypervisor's LAN IP).

Routed networks require `net.ipv4.ip_forward = 1` on the hypervisor. The role sets this (persisted under `/etc/sysctl.d/99-libvirt-routed-networks.conf` and applied immediately) whenever any `libvirt_net_*` definition uses `forward_mode: route`; set `libvirt_enable_ip_forward: false` to opt out if forwarding is already managed elsewhere.

### Guest domains

Each guest is an inventory host in `libvirt_guest_group`. Its own hostvars, any key matching `^libvirt_.*$`, are collected and the `libvirt_` prefix stripped to build the domain definition — the same pattern `vmutti.vagrant.deploy` uses for `vagrant_*` guest vars.

`libvirt_hypervisor` (required): identifies which hypervisor should deploy this guest — must equal that hypervisor's `libvirt_hypervisor_identifier` (its `inventory_hostname` by default).

    libvirt_hypervisor: dev.Thiala.local.vmutti.com
    libvirt_memory_mb: 2048
    libvirt_vcpus: 2
    libvirt_disk_path: /var/lib/libvirt/images/guests/example.qcow2
    libvirt_network: guests
    libvirt_autostart: true

Other guest keys: `uuid`, `memory_mb` (default `1024`), `vcpus` (default `1`), `arch` (default `x86_64`), `machine` (default `pc`), `boot_dev` (default `hd`), `disk_path`, `disk_format` (default `qcow2`), `disk_bus` (default `virtio`), `cdrom_path`, `network` (default `default`), `mac`, `static_ip`, `nic_model` (default `virtio`), `graphics_type` (default `vnc`), `graphics_listen` (default `0.0.0.0`), `video_model` (default `qxl`), `autostart` (default `false`), `state` (default `libvirt_guest_default_state`), `volumes` (see below).

### Extra storage volumes

Set `libvirt_volumes` on a guest (a plain list, copied through as-is by the `^libvirt_.*$` prefix-strip) to attach one or more additional disks backed by volumes in one of this hypervisor's `libvirt_pool_*` pools:

    libvirt_volumes:
      - pool: storage
        name: example.prod.Galaderon.local.vmutti.com-storage.qcow2
        capacity_gb: 500
        target_dev: vdb

Volume keys: `pool` (required, must match a `libvirt_pool_*` name on this hypervisor), `name` (required — the volume's filename inside the pool; give it something predictable, e.g. derived from the guest name, so it's identifiable with `virsh vol-list <pool>`), `capacity_gb` (required), `target_dev` (required — the guest-visible device, e.g. `vdb`), `format` (default `qcow2`), `bus` (default `virtio`), `permissions.{owner,group,mode}` (per-volume override of `libvirt_volume_owner`/`libvirt_volume_group`/`libvirt_volume_mode` below).

The role creates each referenced volume (via `virt_volume`, idempotent — reruns won't recreate or shrink it) before defining any domains, then attaches it to the domain XML as a pool-backed `<disk type="volume">`, not a `<disk type="file">`. This matters for deletion: `vmutti.libvirt.destroy`'s `libvirt_destroy_remove_storage`/`delete_volumes` flag only ever deletes `file`-backed disk sources (the guest's own `disk_path`/`cdrom_path`) — pool-backed volumes are never touched by it and survive undefining the domain. Remove one explicitly with `virt_volume` (`state: absent`) if you actually want it gone.

#### Volume ownership

A freshly created volume is owned `root:root 0600` by default, and libvirt's `dynamic_ownership` relabeling (which normally chowns a domain's disks to the configured qemu user/group right before it starts) does not reliably reach pool-backed `<disk type="volume">` sources the way it does plain `<disk type="file">` sources — the guest's own `disk_path` disk gets relabeled fine, but a first boot referencing a fresh `libvirt_volumes` entry can fail with qemu erroring `Could not open '...': Permission denied`. The role doesn't depend on libvirt to fix this: after creating each volume it resolves the real path with `virsh vol-path` and `chown`/`chmod`s it directly, every run (not just on creation), to `libvirt_volume_owner`/`libvirt_volume_group`/`libvirt_volume_mode` (default `libvirt-qemu`/`kvm`/`0660`, matching Debian's default `/etc/libvirt/qemu.conf`). Override those role variables if a hypervisor's `qemu.conf` sets a different `user`/`group`, or set `permissions.{owner,group,mode}` on an individual volume to override just that one.

### AppArmor and custom pool paths

On Debian, `libvirtd` itself runs under its own enforcing AppArmor profile (`/etc/apparmor.d/usr.sbin.libvirtd`), separate from the per-domain qemu profile `virt-aa-helper` generates when a guest starts. That daemon profile's default allowlist only covers well-known paths like `/var/lib/libvirt/images/**` — a `libvirt_pool_*` pool whose `target_path` lives somewhere else (e.g. a second disk mounted at `/var/lib/libvirt/pools/storage`) isn't on it, so starting a guest with a disk in that pool can fail with a bare `Could not open '...': Permission denied` even though the file's own ownership/mode is already correct (see [Volume ownership](#volume-ownership) above) — this is a separate failure mode from that one, at the daemon's confinement layer rather than plain file permissions.

The role handles this itself: after building storage pools it writes an AppArmor local override (`/etc/apparmor.d/local/usr.sbin.libvirtd`, inside an ansible-managed block so any other manual additions to that file are left alone) granting `rwk` on every configured pool's `target_path`, and reloads the profile if it changed. This is skipped automatically on hosts without `/etc/apparmor.d/usr.sbin.libvirtd` (i.e. AppArmor isn't confining libvirtd at all); set `libvirt_manage_apparmor_pools: false` to opt out explicitly on a host where it's present but managed some other way.

### Static IPs for guests

Set `static_ip` alongside `mac` on a guest to have it always come up on the same address:

    libvirt_network: lan-routed
    libvirt_mac: "52:54:00:12:34:56"
    libvirt_static_ip: 192.168.60.50

The role turns this into a DHCP host reservation (`ip.dhcp_hosts`, keyed on `mac`) on whichever `libvirt_net_*` definition matches the guest's `libvirt_network`, merging it in alongside any reservations already listed there by hand — the guest still gets its address via DHCP, it just always gets the same one. `mac` is required whenever `static_ip` is set (the role fails the run otherwise, since a reservation needs something to bind to), and the target network must be one of this hypervisor's `libvirt_net_*` definitions with `ip.dhcp_range` configured (not the built-in `default` network, which the role never redefines) — the role fails the run with a clear message if either isn't true.

### Disk image upload

If a guest sets `image_path` alongside `disk_path`, the role copies the qcow2 (or other disk image) at `image_path` — resolved on the Ansible controller, e.g. a Packer build under `PackerImages/builds/<location>/<stage>/<image>/libvirt/<image>` — to `disk_path` on the hypervisor before domains are defined, creating `disk_path`'s parent directory first if needed. The `copy` module skips the transfer on later runs when the destination already matches. Omit `image_path` for guests whose disk is provisioned some other way.

    libvirt_image_path: "{{ libvirt_images_path }}/worchestation-debian-libvirt/libvirt/worchestation-debian-libvirt"
    libvirt_disk_path: /var/lib/libvirt/images/guests/example.qcow2

Dependencies
------------

`community.libvirt`

Example Playbook
-----------------

    - hosts: "{{ target_hosts | default('all') }}:&libvirt_hypervisor"
      roles:
        - vmutti.libvirt.deploy

Run against a single hypervisor with `-e target_hosts=dev.Thiala.local.vmutti.com` (or `--limit`); the role only defines guests whose `libvirt_hypervisor` matches the hypervisor(s) actually being played.

License
-------

MIT

Author Information
------------------

Shoshana Makinen, [blog.vmutti.com](https://blog.vmutti.com)
