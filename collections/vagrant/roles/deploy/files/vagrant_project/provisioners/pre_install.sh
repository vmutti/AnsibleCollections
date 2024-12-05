#!/bin/sh
sudo resize2fs /dev/sda1

while sudo fuser /var/lib/dpkg/lock >/dev/null 2>&1 ; do
  sleep 1
done

while sudo fuser /var/lib/apt/lists/lock >/dev/null 2>&1 ; do
  sleep 1
done

if [ -f /var/log/unattended-upgrades/unattended-upgrades.log ]; then
  while sudo fuser /var/log/unattended-upgrades/unattended-upgrades.log >/dev/null 2>&1 ; do
    sleep 1
  done
fi

sudo apt-get update
sudo apt-get upgrade -y --with-new-pkgs
sudo apt autoremove -y

