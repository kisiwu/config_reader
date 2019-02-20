import pytest
import unittest

import settings.reader
from settings.reader import Reader

file_path = "settings" #settings.ini

# Inheriting from TestCase
class Config(unittest.TestCase):

    # initialization
    def setUp(self):
        pass

    # read/create settings file and add missing sections
    def test_direct_read(self):
        cfg = settings.reader.read(file_path, (
            "GLOBAL", 
            ("env_one", { "var_one": "twinkle", "var_two": "dipsy" }),
            ("env_two", { "var_one": "lala", "var_two": "po", "number_one": 1 })
            ))
        self.assertEquals(int(cfg.get_section_options("env_two")["number_one"]), 1)

    # add missing sections without updating file
    def test_no_file_update(self):
        cfg = settings.reader.read(file_path, (
            ("just_invented", { "places": 255, "curr": 8, "name": "random" }),
            ), False)
        just_invented_settings = cfg.get_section_options("just_invented")
        self.assertEquals(int(just_invented_settings["places"]), 255)
        self.assertEquals(int(just_invented_settings["curr"]), 8)
        self.assertEquals(just_invented_settings["name"], "random")

        cfg_2 = settings.reader.read(file_path, (
            ("just_invented", { "places": 4, "curr": 1 }),
            ), False)
        just_invented_settings_2 = cfg_2.get_section_options("just_invented")
        self.assertEquals(int(just_invented_settings_2["places"]), 4)
        self.assertEquals(int(just_invented_settings_2["curr"]), 1)

    # add missing sections and update file
    def test_file_update(self):
        cfg = settings.reader.read(file_path, (
            ("just_invented_updated", { "places": 2, "curr": 2 }),
            ),True)
        just_invented_settings = cfg.get_section_options("just_invented_updated")
        self.assertEquals(int(just_invented_settings["places"]), 2)
        self.assertEquals(int(just_invented_settings["curr"]), 2)

        cfg_2 = settings.reader.read(file_path, (
            ("just_invented_updated", { "places": 18000, "curr": "dfdgery" }),
            ), True)
        just_invented_settings_2 = cfg_2.get_section_options("just_invented_updated")
        self.assertEquals(int(just_invented_settings_2["places"]), 2)
        self.assertEquals(int(just_invented_settings_2["curr"]), 2)

    # arg 2 as 1 tulpe (str, dict)
    def test_arg_2_sections_simple_tulpe(self):
        cfg = settings.reader.read(file_path,
            ("just_invented", { "places": 5, "curr": 4, "name": "random" })
            , False)
        just_invented_settings = cfg.get_section_options("just_invented")
        self.assertEquals(int(just_invented_settings["places"]), 5)
        self.assertEquals(int(just_invented_settings["curr"]), 4)
        self.assertEquals(just_invented_settings["name"], "random")

    # directly instantiate Reader class
    def test_reader_instantiate(self):
        cfg = Reader(file_path,(
            ("just_invented", { "places": 255, "curr": 8, "name": "random" }),
            ), False)
        just_invented_settings = cfg.get_section_options("just_invented")
        self.assertEquals(int(just_invented_settings["places"]), 255)
        self.assertEquals(int(just_invented_settings["curr"]), 8)
        self.assertEquals(just_invented_settings["name"], "random")

    # cleanup actions
    def tearDown(self):
        pass

# boiler plate code to run the test suite
if __name__ == "__main__":
    unittest.main()