#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `rl_generator.utils` module."""


import unittest

from rl_generator import utils


class TestUtils(unittest.TestCase):
    """Tests for `rl_generator` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_randint(self):
        """Test randint function."""
        number = utils.randint(1, 10)
        self.assertGreaterEqual(number, 1)
        self.assertLessEqual(number, 10)


if __name__ == '__main__':
    unittest.main(verbosity=2)
