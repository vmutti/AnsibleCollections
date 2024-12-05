
sudo apt install -y ruby

once="$HOME/.once/autochrome-install"
mkdir -p "$HOME/.once"
if [ ! -f "$once" ]; then
  cd /tmp
  git clone https://github.com/nccgroup/autochrome.git
  cd autochrome
  rm -rf ~/.config/autochrome/
  sudo -H -u vagrant ruby autochrome.rb -c
  touch "$once";
fi
