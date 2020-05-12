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
        settings = utils.Settings()
        settings.load("tests/settings-save-folder.txt")
        self.folder = os.path.expanduser(settings.retrieve("Save-folder"))
        get_episode._download("https://example.com", self.number, folder=self.folder)
        print(f"{self.folder}/p{self.number}.mp3")
        self.assertTrue(os.path.isfile(f"{self.folder}/p{self.number}.mp3"))


class TestNoSaveFolder(unittest.TestCase):
    def tearDown(self):
        get_episode.cleanup(1000)

    def test_no_save_folder(self):
        get_episode._download("https://example.com", 1000)
        self.assertTrue(os.path.isfile("p1000.mp3"))
