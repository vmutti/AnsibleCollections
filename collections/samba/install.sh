#!/bin/sh

sudo apt-get -y install samba


configtar="$HOME/configs/samba/config.tar.gz"

if [ -f "$configtar" ]; then
  sudo tar -xzf "$configtar" -C /
  if [ -f "/tmp/users.backup.tdb" ]; then
    sudo pdbedit -i smbpasswd:/tmp/users.backup.tdb
  fi
fi

sudo cp $HOME/configs/samba/smb.conf /etc/samba/smb.conf
