vmutti.jellyfin.install
========================

Adds Jellyfin's official apt repository, installs the `jellyfin` package (which pulls in `jellyfin-server`, `jellyfin-web`, and `jellyfin-ffmpeg`), enables/starts the `jellyfin` service, and optionally configures hardware-accelerated (VAAPI) transcoding.

Requirements
------------

Debian-based distro with apt (Debian, Ubuntu, or Kali — Kali is treated as Debian bookworm since Jellyfin does not publish a `kali-rolling` repo). The target host must be a member of the `host_install_jellyfin` group.

Role Variables
--------------

`jellyfin_hardware_acceleration_enabled`: whether to install VAAPI drivers and add the `jellyfin` system user to the groups needed for hardware transcoding, default `false`.

`jellyfin_hardware_acceleration_packages`: apt packages installed when hardware acceleration is enabled, default `intel-media-va-driver-non-free`, `vainfo`. Override this for AMD (`mesa-va-drivers`) or Nvidia GPUs.

`jellyfin_hardware_acceleration_groups`: groups the `jellyfin` system user is added to when hardware acceleration is enabled, default `video`, `render`. These grant access to `/dev/dri` for VAAPI.

Dependencies
------------

N/A

Example Playbook
-----------------

    - hosts: host_install_jellyfin
      vars:
        jellyfin_hardware_acceleration_enabled: true
      roles:
         - role: vmutti.jellyfin.install

Notes
-----

- Jellyfin listens on `8096` (HTTP) and `8920` (HTTPS) by default, plus `1900/udp` and `7359/udp` for network discovery. This role does not manage firewall rules; open the relevant ports for the target host's firewall/security group as appropriate.
- Initial server setup (admin account, libraries, transcoding settings) is completed through Jellyfin's web UI on first run and is intentionally left out of this role.
- If `jellyfin_hardware_acceleration_enabled` changes after the service is already running, the `jellyfin` service should be restarted for the new group membership to take effect.

License
-------

MIT

Author Information
------------------

Shoshana Makinen, [blog.vmutti.com](https://blog.vmutti.com)
