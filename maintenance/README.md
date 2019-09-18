# Maintenance

*This directory contains scripts that are only
interesting if you maintain the project.*  

### Keeping the tool list up to date  
[toollist.py](toollist.py) fetches the current tool list from [tools.kali.org/tools-listing](http://tools.kali.org/tools-listing).  
Since the Kali website does not provide a JSON-API or anything like that the script has to parse the HTML of the website to get the current packages.
It outputs a diff that indicates which packages have to be added (with a plus-sign) and which packages have to be removed (with a minus-sign).    
__But:__ Since not all tools on the website are available in the repositories and the package names from the repository might differ from the names on the website there will always be some differences in the package lists.


### Checking available packages
[search.py](search.py) provides a CLI for searching the kali repository.  

[missing.py](missing.py) analyzes katoolin3's package list and checks that all packages from its list are available in the repositories.

### A normal workflow:
- Start [toollist.py](toollist.py) to see what packages have to be removed or added. 
- First remove all packages that have to be removed.   
- Then start [search.py](search.py) and search for the package names which shall be added.  
- The package names that [search.py](search.py) might spit out are added to the package list.  
- Finally execute [sort.py](sort.py) and copy the result into the source file.  
- Have a coffee.