#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

import os
import io
import runpy
from setuptools import setup, find_packages


current = os.path.realpath(os.path.dirname(__file__))

with io.open(os.path.join(current, 'README.rst'), encoding="utf-8") as f:
    long_description = f.read()

with io.open(os.path.join(current, 'HISTORY.rst'), encoding="utf-8") as f:
    history = f.read()

with open(os.path.join(current, 'requirements.txt')) as f:
    requirements = f.read().splitlines()

__version__ = runpy.run_path(
    os.path.join(current, "rl_generator", "version.py"))["__version__"]


setup(
    name='rl_generator',
    author="Fedele Mantuano",
    author_email='mantuano.fedele@gmail.com',
    maintainer="Fedele Mantuano",
    maintainer_email='mantuano.fedele@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Generator of random logs for multiple types of technologies",
    entry_points={
        'console_scripts': [
            'rl_generator=rl_generator.cli:main',
        ],
    },
    platforms=["Linux"],
    install_requires=requirements,
    long_description=long_description + '\n\n' + history,
    include_package_data=True,
    keywords=['log', 'generator', 'random'],
    packages=find_packages(include=['rl_generator']),
    setup_requires=requirements,
    url='https://github.com/fedelemantuano/rl_generator',
    version=__version__,
    zip_safe=False,
)
