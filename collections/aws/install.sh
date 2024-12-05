#!/bin/bash
cd /tmp
curl --silent "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip -qq awscliv2.zip
sudo ./aws/install --update

cd $HOME
virtualenv -p python3 scoutsuite
. scoutsuite/bin/activate
pip3 install scoutsuite
deactivate
