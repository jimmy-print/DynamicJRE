import unittest
import os

import get_episode
import utils
from .abstract_testcase import CreateDeleteSettingsFile

headers = {
    "Range": "bytes=0-100"
}

number = 1000


def make_test_request(self):
    get_episode.download(
        number, get_episode.REGULAR,
        folder=self.folder, headers=headers)


class TestSaveFolder(CreateDeleteSettingsFile):
    def setUp(self):
        self.setUpFunc("tests/settings-save-folder.txt", "Save-folder ~/Desktop")

    def tearDown(self):
        self.tearDownFunc(
            extra_func=lambda: get_episode.cleanup(number, folder=self.folder))

    def test_save_folder(self):
        self.folder = os.path.expanduser(utils.get_save_folder(self.settings_file))
        print(f"{self.folder}/p{number}.mp3")
        make_test_request(self)
        self.assertTrue(os.path.isfile(f"{self.folder}/p{number}.mp3"))


class TestNoSaveFolder(CreateDeleteSettingsFile):
    def setUp(self):
        self.setUpFunc("tests/settings-no-save-folder.txt", "Save-folder ~/Desktop")

    def tearDown(self):
        self.tearDownFunc(
            extra_func=lambda: get_episode.cleanup(number, folder=self.folder))

    def test_no_save_folder(self):
        self.folder = os.path.expanduser(utils.get_save_folder("tests/settings-no-save-folder.txt"))
        make_test_request(self)
        self.assertTrue(os.path.isfile(f"{self.folder}/p{number}.mp3"))


class TestCleanup(CreateDeleteSettingsFile):
    def setUp(self):
        self.setUpFunc("tests/settings-cleanup.txt", "Save-folder ~/Desktop")

    def tearDown(self):
        self.tearDownFunc()

    def test_cleanup(self):
        self.folder = os.path.expanduser(utils.get_save_folder(self.settings_file))
        make_test_request(self)
        get_episode.cleanup(number, folder=self.folder)
        self.assertFalse(os.path.isfile(f"{self.folder}/p{number}.mp3"))


class TestGetLatestEp(CreateDeleteSettingsFile):
    def setUp(self):
        self.setUpFunc("tests/settings-get-latest-ep.txt", "Save-folder ~/Desktop")

    def tearDown(self):
        self.tearDownFunc()

    def test_get_latest_ep_attrs(self):
        episode_num, episode_type = get_episode.get_latest_episode_attributes()
        int(episode_num)
        self.assertTrue(episode_type, get_episode.episode_types)

    def test_get_latest_ep(self):
        folder = os.path.expanduser(utils.get_save_folder(self.settings_file))
        episode_num_alt, __ = get_episode.latest(folder=folder, headers=headers)
        get_episode.cleanup(episode_num_alt, folder=folder)


if __name__ == "__main__":
    main()
