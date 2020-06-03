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


def get_settings(settings_path):
    with open(get_absolute_path(settings_path), 'r') as f:
        raw_file = f.read()

    lines = raw_file.split("\n")

    settings = {}
    for line in lines:
        if len(line.split()) == 2:
            key, value = line.split()
            settings[key] = value

    return settings


def get_save_folder(path="settings.txt"):
    settings = get_settings(path)
    try:
        folder = os.path.expanduser(settings["Save-folder"])
    except KeyError:
        folder = os.path.dirname(get_absolute_path(__file__))
    except FileNotFoundError:
        folder = os.path.dirname(get_absolute_path(__file__))
        print("Please run ./setup, to generate a settings file.")
    return folder 
