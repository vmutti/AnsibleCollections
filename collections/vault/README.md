# server-install
installs the vault binaries required for running a vault deployment
sets up services and permissions necessary for vault to run

# server-tls-disable
sets up a config to let vault run on localhost without proper TLS keys temporarily while it gets setup

# server-db-create
calls the vault operator to actually initialize a new vault database
provides an unseal token and root token, which it should output

# server-unseal
calls the vault API to unseal the vault
needs unseal token

# server-db-init
runs terraform to apply configurations to an unsealed vault server
needs root token

# server-tls-bootstrap
Calls the Vault API to fetch TLS keys and store them on a tempfs.
Then copies a config to the vault server to use the keys to enable a TLS connection and restarts the server

# vagrant-server-install.yml
  server-install

# server-provision
  server-tls-disable
  server-db-create
  server-unseal
  server-db-init
  server-tls-bootstrap

# bootstrap
  server-tls-disable
  server-unseal
  server-tls-bootstrap
