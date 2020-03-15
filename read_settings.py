with open("settings.txt",'r') as f:
    raw_file = f.read()

lines = raw_file.split("\n")

settings = dict()
for line in lines:
    key, value = None, None
    try:
        key, value = line.split()
    except ValueError:
        # there is formatting whitespace
        break
    settings[key] = value

print(settings)
