# -*- coding: utf-8 -*-

"""Console script for rl_generator."""


import click

from . import rl_generator


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
def main(patterns, max_concur_req):
    """Random Logs Generator Tool."""

    rl_generator.core(
        path_patterns=patterns,
        max_concur_req=max_concur_req)


if __name__ == "__main__":
    main()  # pragma: no cover
