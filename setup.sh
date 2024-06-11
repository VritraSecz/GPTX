#!/bin/bash
# https://github.com/VritraSecz
# Code By: VritraSecz
# Don't be copycat create your own

# Printing banner
echo
cat config/banr
# Check if we're running on Termux
if [ -f "/data/data/com.termux/files/usr/bin/termux-info" ]; then
    # Install on Termux
    echo -e "\033[1;91m[~] \033[1;92mInstalling on Termux..."
    echo
    apt update -y
    apt upgrade -y
    apt update -y
    apt upgrade -y
    apt install python -y
    apt install python-pip -y
    pip install openai==0.28
    echo
    echo -e "\033[1;91m[+]\033[1;92m Installation is completed"
    echo -e "\033[1;91m[+]\033[1;92m Type \033[1;91mgptx\033[1;92m command to launch GPTX"
    echo

else
    # Unsupported OS
    echo
    echo -e "\033[1;91m[!] Unsupported OS."
    echo
fi

