# -*- coding: utf-8 -*-

"""Main module."""


import logging
import os
import time

# from tqdm import tqdm

from . import utils


TEMPLATE = "template"
RAW = "raw"


log = logging.getLogger(__name__)


def log_generator(pattern_conf):
    """This function generates a random log file from
    configuration pattern

    Arguments:
        pattern_conf {obj} -- Python object of configuration pattern

    Returns:
        str -- name of logging pattern
    """
    name = pattern_conf["name"]
    path = pattern_conf["path"]
    log_path = os.path.dirname(path)
    log.debug(f"[{name}] - Generating logging for {name}")
    log.debug(f"[{name}] - Generating logging in {path}")
    eps = pattern_conf.get("eps", 1)
    log.debug(f"[{name}] - EPS: {eps}")
    time_period = pattern_conf.get("time_period", 60)
    log.debug(f"[{name}] - time period: {time_period}")
    generator_type = pattern_conf.get("generator_type", "raw")
    print(generator_type)
    log.debug(f"[{name}] - generator type: {generator_type}")

    # calculate nr logs and sleep
    nr_logs = eps * time_period
    sleep_time = 1 / eps

    # create folder log
    if not os.path.exists(log_path):
        os.makedirs(log_path)

    if generator_type == TEMPLATE:
        template = pattern_conf["template"]
        log.debug(f"[{name}] - template: {template}")
        fields = pattern_conf["fields"]

        with open(path, "w") as f:
            for i in range(nr_logs):
                log_str = utils.get_template_log(template, fields)
                f.write(log_str + "\n")
                time.sleep(sleep_time)
    return name
