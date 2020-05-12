import unittest
import os

import utils


class TestKeyError(unittest.TestCase):
    def test_key_error_fail(self):
        settings = utils.Settings()
        settings.load("settings.txt")
        self.assertRaises(KeyError, settings.retrieve, "nonexistent-key")


class TestEnabledKeys(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
