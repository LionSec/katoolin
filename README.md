# katoolin3
Katoolin3 brings all programs available in Kali Linux to Debian and Ubuntu.

### Description
This program is a port of [katoolin](https://github.com/LionSec/katoolin) from [LionSec](https://github.com/LionSec) to python3. Katoolin3 offers several improvements over katoolin:
- __Improved handling of missing packages__   
The old katoolin breaks if a package isn't available in the repositories anymore. Katoolin3 detects those and simply removes them from its package list.

- __Removal of packages__    
You can now remove all packages installed by katoolin3 (individually or all at once).

- __Upgrading wont break your system anymore__   
...because the Kali repositories only get enabled for installing/uninstalling.

- __Better utilization of the APT ecosystem__   
The old katoolin does potentially dangerous operations such as modifying and *deleting* important system configuration files. This has been changed.

- __Easier maintenance of Kalis packages__   
The old katoolin makes it difficult to add new packages to the package list due to the way katoolin was programmed. Changing the package list is now a lot easier.

- __Cleaner code__   
Due to poor code quality katoolin was unmaintainable and had to be rewritten from scratch. katoolin3 aims to be more readable and easier to maintain.

### Requirements
- Aptitude as a package manager
- Python 3.7
- Root privileges

### Usage
Just start the program and follow the instructions ;)

### Something doesn't work?
Hit me up on [Github](https://github.com/s-h-3-l-l/katoolin3/issues/new/choose).