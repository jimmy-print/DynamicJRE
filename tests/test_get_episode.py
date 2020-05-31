import unittest
import os
import requests

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


class TestUnsupportedEpisode(unittest.TestCase):
    def test_unsupported_episode(self):
        return_code = get_episode._download("http://traffic.libsyn.com/joeroganexp/p000.mp3", 0)
        self.assertEqual(return_code, 404)


class TestCleanup(unittest.TestCase):
    def setUp(self):
        self.settings_file = "tests/settings-cleanup.txt"
        self.number = 1000
        with open(self.settings_file, 'w'):
            pass

    def tearDown(self):
        os.remove(self.settings_file)

    def test_cleanup(self):
        self.folder = os.path.expanduser(utils.get_save_folder(self.settings_file))
        get_episode._download("https://example.com", self.number, folder=self.folder)
        get_episode.cleanup(self.number, folder=self.folder)
        self.assertFalse(os.path.isfile(f"p{self.number}.mp3"))


class TestGetLatestEpNumber(unittest.TestCase):
    def test_get_latest_ep_number(self):
        num = get_episode.get_latest_episode_number()
        print(num)
        int(num)
        # There is no self.assertDoesNotRaise in unittest, so this will
        # cause an error instead of a failure if the test fails, as if
        # the test itself was broken.
