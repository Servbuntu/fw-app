#!/bin/zsh
sudo apt-get install -y ufw
if [ $? -ne 0 ]; then
  echo "Failed to install ufw"
  # exit 1
fi
mkdir /serv/pkgs/fw
mkdir -p /serv/data/fw
git clone https://github.com/Servbuntu/fw-app.git /serv/pkgs/fw/
