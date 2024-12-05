#!/bin/sh

once="$HOME/.once/storage-mount"
mkdir -p "$HOME/.once"
if [ ! -f "$once" ]; then
  sudo mkfs -t ext4 /dev/sdb
  sudo mkdir /storage
  sudo mount /dev/sdb /storage -t ext4
  sudo chown -R vagrant:vagrant /storage
  echo "/dev/sdb /storage ext4 defaults 0 0" | sudo tee -a /etc/fstab
  touch "$once";
fi
