import subprocess
import os

import utils

print("Creating symbolic link")
subprocess.run(["ln", "-s", "$(pwd)/jrep.py", "/usr/local/bin/jrep"])
print()

print("Creating settings file")
if os.path.isfile(utils.get_absolute_path("settings.txt")):
    print("File exists.")
else:
    with open(utils.get_absolute_path("settings.txt"), 'w') as f:
        pass
print()

print("Setup complete.")
