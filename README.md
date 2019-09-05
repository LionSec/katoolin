# katoolin3
Katoolin3 brings all programs available in Kali Linux to Debian and Ubuntu.

### Description
This program is a port of [katoolin](https://github.com/LionSec/katoolin) from [LionSec](https://github.com/LionSec) to python3. It has several improvements over katoolin such as
- __Improved handling of missing packages__   
The old katoolin breaks if a package isnt available in the repositories anymore. katoolin3 simply removes those packages from its package list.

- __Easier maintenance of Kalis packages__   
The old katoolin makes it difficult to add new packages to the package list due to the way katoolin was programmed. This has been fixed by katoolin3.

- __Better utilization of the APT ecosystem__   
The old katoolin does potentially dangerous operations such as modifying/*deleting* important system configuration files. This has also been fixed.

- __Cleaner code__   
Due to poor code quality katoolin was unmaintainable and had to be rewritten from scratch. katoolin3 aims to be more readable and easier to maintain.

### Requirements
- aptitude as a package manager
- python3
- root privileges

### Usage
Just start the program and follow the instructions ;)

### Something doesnt work?
Hit me up on [Github](https://github.com/s-h-3-l-l/katoolin3/issues/new/choose).