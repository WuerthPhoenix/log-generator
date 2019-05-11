# Random Log Generator

Generator of random logs for multiple types of technologies.

This tool can generate all kinds of logs starting from templates.
Foreach log you should create a pattern file in YAML format, like in [conf](conf/) folder examples.

If more than one patterns are specified, the tool runs all in parallel. It's possible to run 100 generating in parallel.


## Install

Clone repository

```
git clone url_repository
```

and install with `setup.py`:

```
$ cd rl_generator

$ python setup.py install
```

or use `pip`:

```
$ pip install file_dist
```


## Pattern file

A pattern file has many parameters that are explain in the examples of this repository.

The tool loads all files with `.yml` extension in `patterns` folder.

The main parameters are:

 - _name_: name of log
 - _enabled_: enable/disable this pattern
 - _path_: path where store the log
 - _eps_: number of logs per seconds that will be generate
 - _correction_: eps correction percentage
 - _time_period_: how many seconds the generating is active
 - _generator_type_: you can choose which generator use. The common value is `template`, that generate the logs from a template
 - _examples_: logs of examples
 - _template_: template to use to generate logs
 - _fields_: fields used in template

We can have two kinds of fields:
 - _list_: the list fields are used to generate random values from a given list
 - _func_: the func fields enable functions to generate the random values.

The `func` fields start with `func_` and then have the name of function and parameters.

The `func` developed are:
 - `func_randip`: generate a random ip address
 - `func_randint`: generate a random integer from _min_ to _max_


## Command line

The installation stores on system the `rl_generator` command line.

```
 $ rl_generator --help
Usage: rl_generator [OPTIONS]

  Random Logs Generator Tool.

Options:
  -p, --patterns TEXT             Path all log patterns files (only *.yml)
                                  [default: /home/fedelemantuano/.config/rl_ge
                                  nerator/patterns]
  -m, --max-concur-req INTEGER    Max concurrent logs generating  [default:
                                  10]
  -l, --log-level [CRITICAL|ERROR|WARNING|INFO|DEBUG|NOTSET]
                                  Log level on stdout  [default: WARNING]
  --progress-bar / --no-progress-bar
                                  Enable/Disable progress bar  [default:
                                  False]
  --help                          Show this message and exit.

```


## Features

 - Random logging from template
 - Template can be a list of more formats


## TODO

 - Generate logs from raw examples
 - Generate logs from kv
 - Send logs on network (ssh)