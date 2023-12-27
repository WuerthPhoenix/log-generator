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

"""Utils module for rlog_generator."""


import datetime
import logging
import random
import sys
from faker import Faker

import yaml


log = logging.getLogger(__name__)
fake = Faker()

# TODO Implement possibility to seed for repeatable datasets


def load_config(yaml_file):
    """Return a Python object given a YAML file

    Arguments:
        yaml_file {str} -- path of YAML file

    Returns:
        obj -- Python object of YAML file
    """
    with open(yaml_file, 'r') as f:
        log.debug(f"Loading file {yaml_file}")
        return yaml.load(f, Loader=yaml.FullLoader)


def randint(min_value, max_value):
    """Return random integer in range [min_value, max_value],
    including both end points

    Arguments:
        min_value {int} -- min value
        max_value {int} -- max value

    Returns:
        int -- random integer in range [min_value, max_value]
    """
    return fake.random_int(min=int(min_value), max=int(max_value))

def randmac():
    """Return random MAC address

    Returns:
        str -- MAC address
    """
    return fake.mac_address()

def randip():
    """Return random IP address

    Returns:
        str -- IP address
    """
    return fake.ipv4()

def randuuid():
    """Return random uuid

    Returns:
        str -- uuid
    """
    return fake.uuid4()

def timestamp():
    """Return epoch timestamp

    Returns:
        str -- epoch timestamp
    """
# TODO defaults to random seconds in the last 30 days. Allow parameter change for more flexibility
    return round(fake.unix_time(start_datetime=datetime.timedelta(-30)))


def get_function(function_str, module=sys.modules[__name__]):
    """Return the function from its string name as func_name
    Example: with the name 'func_randint'
    you will get the function name 'randint'

    Arguments:
        function_str {str} -- name of function preceded by 'func_'

    Keyword Arguments:
        module {module obj} -- module object with the function
                                (default: {sys.modules[__name__]})

    Returns:
        obj function -- function of module
    """
    function_str = function_str.split("_")[1]
    return getattr(module, function_str)


def exec_function_str(function_str):
    """Return the value of all string function with/without
    parameters.
    Example: a complete string 'func_randint 1 10' runs the function
    randint(1, 10)

    Arguments:
        function_str {str} -- complete string function

    Returns:
        any -- value of string function
    """
    tokens = function_str.split()
    func = get_function(tokens[0])
    if len(tokens) == 1:
        return func()
    else:
        return func(*tokens[1:])


def get_random_value(field_value):
    """Return the random value of field value in pattern configuration

    Arguments:
        field_value {str/list} -- value of field in pattern configuration

    Raises:
        ValueError: raised when field value is not valid

    Returns:
        any -- random value
    """
    if isinstance(field_value, str):
        return exec_function_str(field_value)
    elif isinstance(field_value, list):
        return random.choice(field_value)
    else:
        raise ValueError('field value can be a string or a list')


def get_template_log(template, fields):
    """Return a random log from template string in Python formatting string
    (https://docs.python.org/3/library/string.html#custom-string-formatting)

    Arguments:
        template {str} -- template string in Python formatting string
        fields {[type]} -- dict field from pattern configuration file

    Returns:
        str -- random log generated from template
    """
    values = {k: get_random_value(v) for k, v in fields.items()}
    now = datetime.datetime.now()
    return template.format(now, **values)


def custom_log(level="WARNING", name=None):  # pragma: no cover
    if name:
        log = logging.getLogger(name)
    else:
        log = logging.getLogger()
    log.setLevel(level)
    ch = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(
        "%(asctime)s | "
        "%(name)s | "
        "%(module)s | "
        "%(funcName)s | "
        "%(levelname)s | "
        "%(message)s")
    ch.setFormatter(formatter)
    log.addHandler(ch)
    return log
