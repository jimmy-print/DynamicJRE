import unittest
import os

import utils


class TestKeyError(unittest.TestCase):
    def setUp(self):
        self.settings_file = "tests/settings-key-error.txt"
        with open("tests/settings-key-error.txt", 'w') as f:
            pass

    def tearDown(self):
        os.remove(self.settings_file)

    def test_key_error(self):
        settings = utils.get_settings(self.settings_file)
        self.assertEqual(settings.get("nonexistent-key"), None)


class TestGetSettings(unittest.TestCase):
    def setUp(self):
        self.settings_file = "tests/settings-get-settings.txt"
        with open(self.settings_file, 'w') as f:
            f.write("Test 1")
        self.settings = utils.get_settings(self.settings_file)

    def tearDown(self):
        os.remove(self.settings_file)

    def test_get_settings(self):
        self.assertTrue("Test" in self.settings)
        self.assertEqual(self.settings.get("Test"), "1")

    def test_get_settings_type(self):
        self.assertEqual(type(self.settings), dict)
        self.assertEqual(type(list(self.settings)[0]), str)
        self.assertEqual(type(self.settings.get("Test")), str)


if __name__ == "__main__":
    unittest.main()
