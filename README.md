![katoolin](https://cloud.githubusercontent.com/assets/8742190/9415562/83397aae-4840-11e5-8f72-28dfffcc70a9.png)
# katoolin
Automatically add the kali repo and install all Kali linux tools

# Features
- Add Kali linux repositories
- Remove kali linux repositories
- Install Kali linux tools

# Requirements
- Python 2.7
- An (debian based) operating system (tested on Ubuntu 20.04)

# Installation
`
sudo su
`

`
apt install python2
`

`
git clone https://github.com/nathmo/katoolin.git && cp katoolin/katoolin.py /usr/bin/katoolin
`

`
chmod +x /usr/bin/katoolin
`

`
sudo katoolin 
`

# Video
https://www.youtube.com/watch?v=8VxCWVoZEEE

# Usage
- Typing the number of a tool will install it
- Typing 0 will install all Kali Linux tools
- back : Go back
- gohome : Go to the main menu
- By installing armitage , you will install metasploit

# Warning
once you installed the tools you needed please remove all Kali-linux repositories as this can seriously fuck up your install if you try to update 

# I have some questions!

Please visit https://github.com/nathmo/katoolin/issues

# Author
this project was forked from https://github.com/LionSec/katoolin/

i just added some fix as the project dont seems to be actively maintained anymore

# TODO
- improve UI (reduce the number of step to install a package, auto add the repo and delete once installed)
- move to python 3
