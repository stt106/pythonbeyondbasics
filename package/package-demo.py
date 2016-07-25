# packages are special modules (which are typically a single source file; represented by class module) in Python and they group relevant modules with similar functionalies together in ways that communicate their cohesiveness and could even contain other packages. Many parts of Python's std library are implemented as packages.'

# A key different between packages and modules are that pacakges have an attribute __path__ whereas modules don't have. __path__ attribute is a list of file system paths indicating where urilib searches to find nested modules. Hence packages are generally represented by directories in the file system while modules are represented by files. To implement a package simply add __init__.py file under the package directory and __init__.py is executed when the package is imported. 

"""
 How does python know where to look for a imported module?
 Ans: Python checks the path attribute of the standard sys module commonly referred to as sys.path which is a list of directories pathon will search for the imported module. It will search the directories one by one until a math is found or raise import error. 
 The first entry is '' which instructs python to search for the current directory. 
 The tail directories contain python std library and the site packages directory where you can install 3rd party libs.

 Sometimes it's necessary to manipulate the sys.path list to make modules available to Python. Another way to make the module available is add the directory to PYTHONPATH environment variable. 

 from package.module import Type/Function --> absolute import 
 from .module import Type/Function ---> relative import; must be within the same level of package/module
 from ..module import Type/Function ---> nested relative import.
 Relative import can reduce typing and enable potential directory change but in general should be avoided!


 __all__ attribute is a list of strings and it decides what import * and if it's unspecified import * will import all public names from the imported module; so it can limite what can be imported from the module. 


 namespace package is a package spreading across a few different directoies with each directory tree contributing to a single logical package. namespace packages don't have __init__.py file to avoid conflicted order of initialisation; hence nothing is executed when the package is imported. Python uses a simple algorithm to find namespace package 'foo' by scanning all directories in the sys.path list 
    1) if a package with __init__.py is found
    2) if a foo.py is found
    3) otherwise all matching **directories** in sys.path are considered part of the namespace package. 


Executable directories contain __main__.py then passing the directory directly into python __main__.py is executed and after that the top level package is imported automatically which means any modules defined within the package can be imported in the __main__.py.
Also python knows how to read executable zip files so it's perfectly sensible to pass in an executable zip file into python directly.


General recommended project layout is:

project-name # root project directory
    __main__.py # make it exectuable
    setup.py # for initial setup
    project_name # package directory
        __init__.py   # as a package
        more_source.py # package modules
        subpackage1 # subpackage directory
            __init__.py # subpackage init
        test # test directory
            __init__.py  # test package init
            test_code.py # testing code 



The simplest way to implement a singlton is using a module as module is only exectued once when first imported. Again _variables are implementation details which shouldn't be accessed directly.
""" 