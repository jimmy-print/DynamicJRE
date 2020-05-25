import unittest
import os

import get_episode
import utils


class TestSaveFolder(unittest.TestCase):
    def setUp(self):
        self.settings_file = "tests/settings-save-folder.txt"
        self.number = 1000
        with open(self.settings_file, 'w') as f:
            f.write(f"Save-folder ~/Desktop")

    def tearDown(self):
        os.remove(self.settings_file)
        get_episode.cleanup(self.number, folder=self.folder)

    def test_save_folder(self):
        self.folder = os.path.expanduser(utils.get_save_folder(self.settings_file))
        get_episode._download("https://example.com", self.number, folder=self.folder)
        print(f"{self.folder}/p{self.number}.mp3")
        self.assertTrue(os.path.isfile(f"{self.folder}/p{self.number}.mp3"))


class TestNoSaveFolder(unittest.TestCase):
    def setUp(self):
        self.settings_file = "tests/settings-no-save-folder.txt"
        self.number = 1000
        with open(self.settings_file, 'w') as f:
            pass

    def tearDown(self):
        os.remove(self.settings_file)
        get_episode.cleanup(self.number, folder=self.folder)

    def test_no_save_folder(self):
        self.folder = os.path.expanduser(utils.get_save_folder("tests/settings-no-save-folder.txt"))
        get_episode._download("https://example.com", self.number, folder=self.folder)
        self.assertTrue(os.path.isfile(f"p{self.number}.mp3"))