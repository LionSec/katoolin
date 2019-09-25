# katoolin3
Katoolin3 brings all programs available in Kali Linux to Debian and Ubuntu.

### Description
This program is a port of [katoolin](https://github.com/LionSec/katoolin) from [LionSec](https://github.com/LionSec) to python3. Katoolin3 offers several improvements over katoolin:
- __Up to date packages__    
The old katoolin uses an outdated package list. Katoolin3 always keeps its package list up to date.

- __Improved handling of missing packages__   
The old katoolin breaks if a package isn't available in the repositories anymore or has some dependency errors. Katoolin3 detects those and simply ignores them.

- __Removal of packages__    
You can now remove all packages installed by katoolin3 (individually or all at once).

- __Upgrading wont break your system anymore__   
...because the Kali repositories only get enabled for installing/uninstalling.

- __Better utilization of the APT ecosystem__   
The old katoolin does potentially dangerous operations such as modifying and *deleting* important system configuration files. This has been changed.

- __Easier maintenance of Kalis packages__   
The old katoolin makes it difficult to add new packages to the package list due to the way katoolin was programmed. Maintaining the package list is now a lot easier.

- __Cleaner code__   
Due to poor code quality katoolin was unmaintainable and had to be rewritten from scratch. katoolin3 aims to be more readable and easier to maintain.

### Requirements
- Aptitude as a package manager
- Python >= 3
- Root privileges
- sh, bash
- python3-apt

### Installation
```bash
git clone https://github.com/s-h-3-l-l/katoolin3;
cd katoolin3;
chmod +x ./install.sh;
sudo ./install.sh;
```

### Usage
The program flow of katoolin3 is realized by presenting
a list of options that you can choose from.
These lists look like that:  
```
0) ...  
1) ...  
2) ...
```
##### Installing tools
To install a package enter the corresponding number.
To install multiple packages at once specify a range like ```3-5```, a list like ```1,2,3``` or combine them like ```1,2,5-7,9```.
You can also install all packages at once.

##### Uninstalling tools
This works just like installing except that you have to prepend a ```~``` before your selection. You can also uninstall all packages at once.

##### Searching
Katoolin3 supports searching the package cache.  
 E.g. if you want to install some tools related to SQL injections you can go into the search menu and search for ```sql injection```. If you want to have specific information about a package just enter the package name in the same search menu.   
   
For more functions see the help dialogue inside the program.

### Updating
To update your tool list execute  
```bash
chmod +x ./update.sh;
sudo ./update.sh;
```  

### Tested on
- Debian 10 (Buster)
- Ubuntu 18.04 LTS
- Ubuntu 19.04

### Something doesn't work?
Hit me up on [Github](https://github.com/s-h-3-l-l/katoolin3/issues/new/choose).

### Uninstalling
To uninstall katoolin3 execute
```bash
chmod +x ./uninstall.sh;
sudo ./uninstall.sh;
```
Uninstalling the Kali tools can be done inside katoolin3.
