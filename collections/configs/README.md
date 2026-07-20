# vmutti.configs

Fetches and archives per-service configuration files (user- and system-level paths) from managed hosts back to the Ansible controller, for the backup/restore workflow used by other `vmutti.*` roles (e.g. `vmutti.alacritty`, `vmutti.tmux`, `vmutti.vim`, `vmutti.xfce`, `vmutti.zsh`). Those roles expose a `fetch_configs.yml` task/defaults hook that this role includes to learn which paths to back up.

## Roles

- [fetch](roles/fetch/README.md) — archives and fetches configured services' user/system paths from a host

## Playbooks

- `playbooks/fetch_configs.yml`: runs `vmutti.configs.fetch` against `{{ target_hosts | default('all') }}:&worchestation` hosts.

## License

MIT
