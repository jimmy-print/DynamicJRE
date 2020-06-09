# DynamicJRE
A command line podcast manager for The Joe Rogan Experience.

### Install
    git clone https://github.com/jimmy-print/DynamicJRE.git
    cd DynamicJRE
    python setup.py
setup.py will:
- Create a symbolic link in /usr/local/bin to jrep.py, named jrep.
- Create settings.txt, in the project folder.
### Usage examples
    jrep --help
    jrep 1255
    jrep latest
I am not affiliated with JRE.

### Todo
For this branch:
- use a proper setup.py with distutils
- create a dynamic_jre folder with module files