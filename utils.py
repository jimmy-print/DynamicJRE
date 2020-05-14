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


class Settings:
    def __init__(self, enabled_keys=None):
        self.settings = {}

        self.enabled_keys = enabled_keys
        if self.enabled_keys is not None:
            assert type(self.enabled_keys) == tuple

    def load(self, settings_path):
        with open(get_absolute_path(settings_path), 'r') as f:
            raw_file = f.read()

        lines = raw_file.split("\n")

        for line in lines:
            if len(line.split()) == 2:
                key, value = line.split()
                if self.enabled_keys is None:
                    self.settings[key] = value
                else:
                    if key in self.enabled_keys:
                        self.settings[key] = value

    def retrieve(self, key):
        return self.settings[key]


def get_save_folder(path="settings.txt"):
    settings = Settings()
    settings.load(path)
    try:
        folder = os.path.expanduser(settings.retrieve("Save-folder"))
    except KeyError:
        folder = os.path.dirname(get_absolute_path(__file__))
    return folder 
