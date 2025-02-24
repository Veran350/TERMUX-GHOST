#!/bin/bash  
termux-wake-lock  
pkg update -y  
pkg install -y git python tor root-repo  
git clone https://github.com/yourusername/TERMUX-GHOST  
cd TERMUX-GHOST  
chmod +x lib/*.sh  
pip install Flask pycryptodome  
./lib/termux_payload.sh  
clear  
echo -e "\e[31m$(cat ghost_banner.txt)\e[0m"  
python main.py  
