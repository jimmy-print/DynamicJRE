import os


def get_absolute_path(relative_path):
    absolute_path_of_program_folder = os.path.dirname(
        os.path.abspath(__file__))
    absolute_path = os.path.join(absolute_path_of_program_folder,
                                 relative_path)
    return absolute_path


def print_usage_message():
    path = f"{get_absolute_path('usage_message.txt')}"
    with open(path, 'r') as f:
        print(f.read())


def get_settings():
    with open(get_absolute_path("settings.txt"), 'r') as f:
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

    return settings
