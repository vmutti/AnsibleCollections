# vmutti.aws

Not yet wrapped as an Ansible role: `install.sh` installs the AWS CLI v2, then creates a `scoutsuite` Python virtualenv (via `virtualenv`/`pip3`) and installs ScoutSuite into it for AWS security auditing.

## Usage

Run `install.sh` on the target host (for example, via Ansible's `script` module) as a user that can `sudo`.

## License

MIT
