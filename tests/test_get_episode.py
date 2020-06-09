import unittest
import os

from dynamic_jre import get_episode

headers = {
    "Range": "bytes=0-100"
}

number = 1000


def make_test_request(self):
    get_episode.download(
        number, get_episode.REGULAR,
        headers=headers)


class TestSaveFolder(unittest.TestCase):
    def tearDown(self):
        get_episode.cleanup(number)

    def test_save_folder(self):
        make_test_request(self)
        self.assertTrue(os.path.isfile(f"p{number}.mp3"))


class TestNoSaveFolder(unittest.TestCase):
    def tearDown(self):
        get_episode.cleanup(number)

    def test_no_save_folder(self):
        make_test_request(self)
        self.assertTrue(os.path.isfile(f"p{number}.mp3"))


class TestCleanup(unittest.TestCase):
    def test_cleanup(self):
        make_test_request(self)
        get_episode.cleanup(number)
        self.assertFalse(os.path.isfile(f"/p{number}.mp3"))


class TestGetLatestEp(unittest.TestCase):
    def test_get_latest_ep_attrs(self):
        episode_num, episode_type = get_episode.get_latest_episode_attributes()
        int(episode_num)
        self.assertTrue(episode_type, get_episode.episode_types)

    def test_get_latest_ep(self):
        episode_num_alt, __ = get_episode.latest(headers=headers)
        get_episode.cleanup(episode_num_alt)


if __name__ == "__main__":
    unittest.main()
