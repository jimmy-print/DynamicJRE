import unittest

import utils
from .abstract_testcase import CreateDeleteSettingsFile


class TestKeyError(CreateDeleteSettingsFile):
    def setUp(self):
        self.setUpFunc("tests/settings-key-error.txt", "tests/settings-key-error.txt")

    def tearDown(self):
        self.tearDownFunc()

    def test_key_error(self):
        settings = utils.get_settings(self.settings_file)
        self.assertEqual(settings.get("nonexistent-key"), None)


class TestGetSettings(CreateDeleteSettingsFile):
    def setUp(self):
        self.setUpFunc("tests/settings-get-settings.txt", "Test 1")
        self.settings = utils.get_settings(self.settings_file)

    def tearDown(self):
        self.tearDownFunc()

    def test_get_settings(self):
        self.assertTrue("Test" in self.settings)
        self.assertEqual(self.settings.get("Test"), "1")

    def test_get_settings_type(self):
        self.assertEqual(type(self.settings), dict)
        self.assertEqual(type(list(self.settings)[0]), str)
        self.assertEqual(type(self.settings.get("Test")), str)


if __name__ == "__main__":
    unittest.main()
