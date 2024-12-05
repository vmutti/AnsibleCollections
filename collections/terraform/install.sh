#!/bin/sh

mod='terraform'
wget https://releases.hashicorp.com/terraform/0.12.23/terraform_0.12.23_linux_amd64.zip -O /tmp/terraform.zip
sudo unzip /tmp/terraform.zip -d /usr/local/bin/
sudo chmod +x /usr/local/bin/terraform

# once="$HOME/.once/$mod-profile"
# mkdir -p "$HOME/.once"
# if [ ! -f "$once" ]; then
#   #TKTK
#   touch "$once";
# fi
