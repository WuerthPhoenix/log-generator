# -*- coding: utf-8 -*-

"""Console script for rl_generator."""


import click

from . import rl_generator
from .utils import custom_log


@click.command()
@click.option(
    '--patterns', "-p",
    default="~/.config/rl_generator/patterns",
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
def main(patterns, max_concur_req, log_level):
    """Random Logs Generator Tool."""

    custom_log(level=log_level)

    total_logs = rl_generator.core(
        path_patterns=patterns,
        max_concur_req=max_concur_req)
    print(f"\nGenerated {total_logs} logs")


if __name__ == "__main__":
    main()  # pragma: no cover
