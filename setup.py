#!/usr/bin/env python3

import subprocess

print("--------------------")

print("Creating symbolic link")
subprocess.run(["ln", "-s", "$(pwd)/jrep.py", "/usr/local/bin/jrep"])
print()

print("Creating settings file")
subprocess.run(["touch", "settings.txt"])
print()

print("Setup complete.")

print("--------------------")
