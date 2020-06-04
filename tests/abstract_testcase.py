import unittest
import os


class CreateDeleteSettingsFile(unittest.TestCase):
    def setUpFunc(self, settings_file_path, settings_text):
        self.settings_file = settings_file_path
        with open(self.settings_file, 'w') as f:
            f.write(settings_text)

    def tearDownFunc(self, extra_func=lambda: None):
        os.remove(self.settings_file)
        extra_func()