# packages are special modules (which are typically a single source file; represented by class module) in Python and they group relevant modules with similar functionalies together in ways that communicate their cohesiveness and could even contain other packages. Many parts of Python's std library are implemented as packages.'

# A key different between packages and modules are that pacakges have an attribute __path__ whereas modules don't have. __path__ attribute is a list of file system paths indicating where urilib searches to find nested modules. Hence packages are generally represented by directories in the file system while modules are represented by files.

"""
 How does python know where to look for a imported module?
 Ans: Python checks the path attribute of the standard sys module commonly referred to as sys.path which is a list of directories pathon will search for the imported module. It will search the directories one by one until a math is found or raise import error. 
 The first entry is '' which instructs python to search for the current directory. 
 The tail directories contain python std library and the site packages directory where you can install 3rd party libs.

 Sometimes it's necessary to manipulate the sys.path list to make modules available to Python. Another way to make the module available is add the directory to PYTHONPATH environment variable. 
""" 