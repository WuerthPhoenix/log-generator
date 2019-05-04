#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `rl_generator` package."""


import os
import unittest

from click.testing import CliRunner

from rl_generator import rl_generator, utils
from rl_generator import cli


class TestRlGenerator(unittest.TestCase):
    """Tests for `rl_generator.rl_generator` module."""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.pattern_file = "tests/conf/patterns/apache_commons.yml"
        self.conf_file = "conf/rl_generator.yml"
        self.pattern = utils.load_config(self.pattern_file)

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_log_generator(self):
        """Test log_generator function."""
        nr_logs = rl_generator.log_generator(self.pattern)
        self.assertEqual(nr_logs, 30)
        self.assertTrue(os.path.exists("/tmp/apache.log"))

        with open("/tmp/apache.log") as f:
            lines = len(f.readlines())

        self.assertEqual(lines, 30)
        self.assertEqual(nr_logs, lines)

    def test_core(self):
        pass

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'rl_generator.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
        print(runner.invoke(cli.main, ['--patterns']))
