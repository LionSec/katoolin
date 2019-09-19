# katoolin3
Katoolin for python3.

### Requirements
- Aptitude as a package manager
- Python 3
- Root privileges
- VT-100 compliant terminal

### Usage
```
The program flow of this program is realized by presenting
a list of options that you can choose from.
These lists look like that:
0) Do A
1) Do B
2) Do C

When selecting packages you can select
more than one by passing a comma-separated list like
'0,1,2,3' or specifying a range like '12-24' or combining
those two '0,1,3-5,12'.

If you want to remove packages simply prepend '~' before a
string like above.

Packages which are already installed are shown in black.

Example:
Select some options with '1,2,8-10'.
Then you realize those programs are shit and you do
'~1,2,8-10' to uninstall them.
Simple as that.
```

### Tested on
- Debian 10 (Buster)
- Ubuntu 18.04 LTS
- Ubuntu 19.04
