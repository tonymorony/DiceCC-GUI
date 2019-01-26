# What Dice CC is?

Almost instant blockchain based game between dealer and player with "decentralized" RNG.

More information can be found here: https://github.com/tonymorony/Mastering_CryptoConditions/blob/RU/all_chapters.md#chapter-9---dice-example
And here: https://github.com/KomodoPlatform/komodo/blob/master/src/cc/dice.cpp

# What this tool do?

This tool is a graphical implementation (buttons and forms hehe)of DiceCC RPC calls.

At the moment it's a prototype / mock so I didn't care about UI beauty at all.

![alt text](https://i.imgur.com/eg1VkDU.png)

# Installation 

Developer installation. Tested on Ubuntu 18.04 (assuming python 3.6+ is installed by default)
And Komodo daemon was built from FSM branch of https://github.com/jl777/komodo/

Pre-built packages are under development.
```
sudo add-apt-repository ppa:kivy-team/kivy
sudo apt-get install python3-pip libssl-dev cython3 libgl-dev git python3-kivy libcurl4-openssl-dev libssl-dev
pip3 install requests wheel python-bitcoinlib slick-bitcoinrpc pygame
git clone https://github.com/tonymorony/DiceCC-GUI
cd DiceCC-GUI
python3 DiceCC.py
```

# RPC Connection

* In case of localhost daemon usage use 127.0.0.1 as RPC address. Username, password and port can be found in .conf file for desired asset chain

* If you want to use remote host for RPC connection you need to add your IP as rpcallowip= param to desired asset chain daemon config

![alt text](https://i.imgur.com/vqeftYW.png)
