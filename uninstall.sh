#!/bin/zsh
sudo apt-get remove -y ufw
if [ $? -ne 0 ]; then
  echo "Failed to remove ufw"
  # exit 1
fi
rm -rf /serv/pkgs/fw/*
