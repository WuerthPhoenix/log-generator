# -*- coding: utf-8 -*-

"""
Copyright 2019 Würth Phoenix S.r.l.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

"""Console script for rlog_generator."""


import runpy
import sys
from os.path import expanduser, join, realpath, dirname

import click

from . import rlog_generator
from .utils import custom_log


current = realpath(dirname(__file__))

__version__ = runpy.run_path(
    join(current, "version.py"))["__version__"]


@click.command()
@click.version_option(version=__version__)
@click.option(
    '--patterns', "-p",
    default=join(expanduser("~"), ".config/rlog_generator/patterns"),
    show_default=True,
    type=str,
    help="Path all log patterns files (only *.yml)")
@click.option(
    '--max-concur-req', "-m",
    default=10,
    show_default=True,
    type=int,
    help="Max concurrent logs generating")
@click.option(
    '--log-level', "-l",
    default='WARNING',
    show_default=True,
    type=click.Choice(
        ['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'NOTSET']),
    help="Log level on stdout")
@click.option(
    '--progress-bar/--no-progress-bar',
    default=False,
    show_default=True,
    help="Enable/Disable progress bar")

def main(patterns, max_concur_req, log_level, progress_bar):
    """Random Logs Generator Tool."""

    custom_log(level=log_level)

    try:
        total_logs = rlog_generator.core(
            path_patterns=patterns,
            max_concur_req=max_concur_req,
            progress_bar=progress_bar)
        print(f"\nGenerated {total_logs} logs")
    except KeyboardInterrupt:  # pragma: no cover
        sys.exit(0)


if __name__ == "__main__":
    main()  # pragma: no cover
