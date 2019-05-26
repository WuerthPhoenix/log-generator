`Build Status <https://travis-ci.org/WuerthPhoenix/log-generator>`__
`Coverage
Status <https://coveralls.io/github/WuerthPhoenix/log-generator?branch=develop>`__

Random Log Generator
====================

Generator of random logs for multiple types of technologies.

This tool can generate all kinds of logs starting from templates.
Foreach log you should create a pattern file in YAML format, like in
`conf <conf/>`__ folder examples.

If more than one patterns are specified, the tool runs all in parallel.
It’s possible to run 100 generating in parallel.

Install
-------

Clone repository

::

   git clone url_repository

and install with ``setup.py``:

::

   $ cd log-generator

   $ python setup.py install

or use ``pip``:

::

   $ pip install rlog-generator

Pattern file
------------

A pattern file has many parameters that are explain in the examples of
this repository.

The tool loads all files with ``.yml`` extension in ``patterns`` folder.

The main parameters are:

-  *name*: name of log
-  *enabled*: enable/disable this pattern
-  *path*: path where store the log
-  *eps*: number of logs per seconds that will be generate
-  *correction*: eps correction percentage
-  *time_period*: how many seconds the generating is active
-  *generator_type*: you can choose which generator use. The common
   value is ``template``, that generate the logs from a template
-  *examples*: logs of examples
-  *template*: template to use to generate logs
-  *fields*: fields used in template

We can have two kinds of fields: - *list*: the list fields are used to
generate random values from a given list - *func*: the func fields
enable functions to generate the random values.

The ``func`` fields start with ``func_`` and then have the name of
function and parameters.

The ``func`` developed are: - ``func_randip``: generate a random ip
address - ``func_randint``: generate a random integer from *min* to
*max*

Command line
------------

The installation stores on system the ``rlog-generator`` command line.

::

    $ rlog-generator --help
   Usage: rlog-generator [OPTIONS]

     Random Logs Generator Tool.

   Options:
     -p, --patterns TEXT             Path all log patterns files (only *.yml)
                                     [default: ~/.config/rlog_generator/patterns]
     -m, --max-concur-req INTEGER    Max concurrent logs generating  [default:
                                     10]
     -l, --log-level [CRITICAL|ERROR|WARNING|INFO|DEBUG|NOTSET]
                                     Log level on stdout  [default: WARNING]
     --progress-bar / --no-progress-bar
                                     Enable/Disable progress bar  [default:
                                     False]
     --help                          Show this message and exit.

Features
--------

-  Random logging from template
-  Template can be a list of more formats

TODO
----

-  Generate logs from raw examples

Apache 2 Open Source License
----------------------------

This tool can be downloaded, used, and modified free of charge. It is
available under the Apache 2 license.
