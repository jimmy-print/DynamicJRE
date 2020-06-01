import unittest
import os
import requests

import get_episode
import utils

headers = {
    "Range": "bytes=0-100"
}

number = 1000


def make_test_request(self):
    get_episode.download(
            number, get_episode.REGULAR,
            folder=self.folder, headers=headers)


class TestSaveFolder(unittest.TestCase):
    def setUp(self):
        self.settings_file = "tests/settings-save-folder.txt"
        with open(self.settings_file, 'w') as f:
            f.write(f"Save-folder ~/Desktop")

    def tearDown(self):
        os.remove(self.settings_file)
        get_episode.cleanup(number, folder=self.folder)

    def test_save_folder(self):
        self.folder = os.path.expanduser(utils.get_save_folder(self.settings_file))
        print(f"{self.folder}/p{number}.mp3")
        make_test_request(self)
        self.assertTrue(os.path.isfile(f"{self.folder}/p{number}.mp3"))


class TestNoSaveFolder(unittest.TestCase):
    def setUp(self):
        self.settings_file = "tests/settings-no-save-folder.txt"
        with open(self.settings_file, 'w') as f:
            pass

    def tearDown(self):
        os.remove(self.settings_file)
        get_episode.cleanup(number, folder=self.folder)

    def test_no_save_folder(self):
        self.folder = os.path.expanduser(utils.get_save_folder("tests/settings-no-save-folder.txt"))
        make_test_request(self)
        self.assertTrue(os.path.isfile(f"p{number}.mp3"))


class TestCleanup(unittest.TestCase):
    def setUp(self):
        self.settings_file = "tests/settings-cleanup.txt"
        with open(self.settings_file, 'w'):
            pass

    def tearDown(self):
        os.remove(self.settings_file)

    def test_cleanup(self):
        self.folder = os.path.expanduser(utils.get_save_folder(self.settings_file))
        make_test_request(self)
        get_episode.cleanup(number, folder=self.folder)
        self.assertFalse(os.path.isfile(f"p{number}.mp3"))


class TestGetLatestEp(unittest.TestCase):
    def test_get_latest_ep_attrs(self):
        episode_num, episode_type = get_episode.get_latest_episode_attributes()
        int(episode_num)
        self.assertTrue(episode_type, get_episode.episode_types)

    def test_get_latest_ep(self):
        episode_num_alt, __ = get_episode.latest(headers=headers)
        get_episode.cleanup(episode_num_alt)
