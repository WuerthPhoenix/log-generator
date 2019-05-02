#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `rl_generator.utils` module."""


import unittest

from rl_generator import utils


class TestUtils(unittest.TestCase):
    """Tests for `rl_generator` package."""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.pattern_file = "conf/patterns/apache_commons.yml"
        self.conf_file = "conf/rl_generator.yml"

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_randint(self):
        """Test randint function."""
        number = utils.randint(1, 10)
        self.assertGreaterEqual(number, 1)
        self.assertLessEqual(number, 10)

    def test_randip(self):
        """Test randip function."""
        ip = utils.randip()
        self.assertIsInstance(ip, str)
        self.assertEqual(len(ip.split(".")), 4)

    def test_get_function(self):
        """Test get_function function."""
        func = utils.get_function("func_randip")
        ip = func()
        self.assertIsInstance(ip, str)
        self.assertEqual(len(ip.split(".")), 4)

        func = utils.get_function("func_randint")
        number = func(1, 10)
        self.assertGreaterEqual(number, 1)
        self.assertLessEqual(number, 10)

    def test_exec_function_str(self):
        """Test exec_function_str function."""
        ip = utils.exec_function_str("func_randip")
        self.assertIsInstance(ip, str)
        self.assertEqual(len(ip.split(".")), 4)
        number = utils.exec_function_str("func_randint 1 10")
        self.assertGreaterEqual(number, 1)
        self.assertLessEqual(number, 10)

    def test_get_random_value(self):
        """Test get_random_value function."""
        with self.assertRaises(ValueError):
            utils.get_random_value({'fake_key': 'fake_value'})

        ip = utils.get_random_value("func_randip")
        self.assertIsInstance(ip, str)
        self.assertEqual(len(ip.split(".")), 4)

        value_list = list(range(10))
        value = utils.get_random_value(value_list)
        self.assertGreaterEqual(value, 0)
        self.assertLessEqual(value, 9)

    def test_get_template_log(self):
        """Test test_get_template_log function."""
        pattern = utils.load_config(self.pattern_file)
        log = utils.get_template_log(
            pattern["template"], pattern["fields"])
        self.assertIsInstance(log, str)
        log_new = utils.get_template_log(
            pattern["template"], pattern["fields"])
        self.assertNotEqual(log, log_new)
        self.assertIn("HTTP/1.0", log)


if __name__ == '__main__':
    unittest.main(verbosity=2)
