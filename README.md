[![Build Status](https://travis-ci.org/WuerthPhoenix/log-generator.svg?branch=develop)](https://travis-ci.org/WuerthPhoenix/log-generator)
[![PyPI version](https://badge.fury.io/py/rlog-generator.png)](https://badge.fury.io/py/rlog-generator)

# Random Log Generator

Generator of random logs for multiple types of technologies.

This tool can generate all kinds of logs starting from templates.
You should create a pattern file in YAML format foreach log that you want to generate, like in [conf/patterns](conf/patterns) examples.

If more than one patterns are specified in patterns folder, all logs are generated in parallel. It's possible to generate 100 logs in parallel.

## Install

Clone repository

```bash
git clone https://github.com/WuerthPhoenix/log-generator.git
```

and install with `setup.py`:

```bash
cd log-generator

python setup.py install
```

or use `pip`:

```bash
pip install rlog-generator
```

## Docker

Clone repository

```bash
git clone https://github.com/WuerthPhoenix/log-generator.git
```

build docker

```bash
docker build -t log-generator:latest .
```

and use it

```bash
docker run -v `pwd`/conf/patterns:/root/.config/rlog_generator/patterns log-generator
```

## Pattern file

A pattern file has many parameters.

| Parameters | Descriptions |
| ---------- | ------------ |
| _name_ | name of log
| _enabled_ | enable/disable this pattern
| _stdout_ | log to stdout instead of file
| _path_ | path where store the log
| _eps_ | number of logs per seconds that will be generate
| _correction_ | eps correction percentage
| _time_period_ | how many seconds the generating is active
| _generator_type_ | you can choose which generator use. The common value is `template`, that generate the logs from a template
| _examples_ | logs of examples
| _template_ | template to use to generate logs
| _fields_ | fields used in template

We can have two kinds of fields:
 - _list_: the list fields are used to generate random values from a given list
 - _func_: the func fields enable functions to generate the random values.

The `func` fields start with `func_` and then have the name of function. It can also have parameters.

The `func` developed are:
 - `func_randip`: generate a random ip address
 - `func_randint`: generate a random integer from _min_ to _max_
 - `func_randmac`: generate a random MAC address
 - `func_randuuid`: generate a random UUID address

For more details see the examples in folder [conf/patterns](conf/patterns).

If you want to contribute with real templates, add them in [patterns](patterns) folder.

## Command line

The installation stores on system the `rlog-generator` command line.

```bash
 $ rlog-generator --help
Usage: rlog-generator [OPTIONS]

  Random Logs Generator Tool.

Options:
  -p, --patterns TEXT             Path all log patterns files (only *.yml)
                                  [default: ~/.config/rlog_generator/patterns]
  -m, --max-concur-req INTEGER    Max concurrent logs generating  [default: 10]
  -l, --log-level [CRITICAL|ERROR|WARNING|INFO|DEBUG|NOTSET]
                                  Log level on stdout  [default: WARNING]
  --progress-bar / --no-progress-bar
                                  Enable/Disable progress bar  [default: False]
  --help                          Show this message and exit.

```

## Features

 - Random logging from template
 - Template can be a list of more formats

## TODO

 - Generate logs from raw examples

## Apache 2 Open Source License
This tool can be downloaded, used, and modified free of charge. It is available under the Apache 2 license.