import unittest
import os

import utils
import get_episode


class TestSettingsKeyError(unittest.TestCase):
    def test_key_error_fail(self):
        settings = utils.Settings()
        settings.load("settings.txt")
        self.assertRaises(KeyError, settings.retrieve, "nonexistent-key")


class TestSettingsEnabledKeys(unittest.TestCase):
    def setUp(self):
        with open("tests/settings-enabled-keys.txt", 'w') as f:
            f.write("Bruh 1")

    def tearDown(self):
        os.remove("tests/settings-enabled-keys.txt")


    def test_enabled_keys_type_fail(self):
        self.assertRaises(AssertionError,
                          utils.Settings,
                          "Incorrect str enabled_keys arg")

    def test_enabled_keys_fail(self):
        settings = utils.Settings((
            "Key-1",
            "Key-2",
            "Key-3",
        ))
        settings.load("tests/settings-enabled-keys.txt")
        self.assertRaises(KeyError, settings.retrieve, "Bruh")


class TestSettingsSaveFolder(unittest.TestCase):
    def setUp(self):
        self.settings_file = "tests/settings-save-folder.txt"
        self.number = 1000
        with open(self.settings_file, 'w') as f:
            f.write(f"Save-folder ~/Desktop")

    def tearDown(self):
        os.remove(self.settings_file)
        get_episode.cleanup(self.number, folder=self.folder)

    def test_save_folder(self):
        settings = utils.Settings()
        settings.load("tests/settings-save-folder.txt")
        self.folder = os.path.expanduser(settings.retrieve("Save-folder"))
        get_episode._download("https://example.com", self.number, folder=self.folder)
        print(f"{self.folder}/p{self.number}.mp3")
        self.assertTrue(os.path.isfile(f"{self.folder}/p{self.number}.mp3"))


if __name__ == "__main__":
    unittest.main()
