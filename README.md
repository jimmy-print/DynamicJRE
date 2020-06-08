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
Add support for non-standard episodes (MMA, Fight Companion).
(This is partially completed. MMA episodes are now supported.)

Use a different file format from plain text to store configuration.
