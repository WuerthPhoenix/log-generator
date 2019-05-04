# -*- coding: utf-8 -*-

"""Main module."""


import glob
import logging
import os
import time

from concurrent import futures

from tqdm import trange

from . import utils


TEMPLATE = "template"
RAW = "raw"
MAX_CONCUR_REQ = 100


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
    log.debug(f"[{name}] - generator type: {generator_type}")
    remove_file = pattern_conf.get("remove_file", False)

    # calculate nr logs and sleep
    nr_logs = eps * time_period
    sleep_time = 1 / eps

    if remove_file:
        try:
            os.remove(path)
        except OSError:
            pass

    # create folder log
    if not os.path.exists(log_path):
        os.makedirs(log_path)

    if generator_type == TEMPLATE:
        template = pattern_conf["template"]
        log.debug(f"[{name}] - template: {template}")
        fields = pattern_conf["fields"]

        for i in trange(nr_logs, desc=f"{name} logs"):
            # for i in range(nr_logs):
            with open(path, "a") as f:
                log_str = utils.get_template_log(template, fields)
                f.write(log_str + "\n")
                time.sleep(sleep_time)
    elif generator_type == RAW:
        pass
    else:
        raise ValueError(f"Generator type {generator_type} doesn't exist")

    return nr_logs


def core(path_patterns, max_concur_req):
    """This function runs the core of tool.
    All threads are generated here. A thread foreach log file.

    Arguments:
        path_patterns {str} -- path of log patterns
        max_concur_req {int} -- max concurrent log generator
    """

    # Load all configuration patterns
    patterns = {
        os.path.basename(i): utils.load_config(i) for i in glob.iglob(
            os.path.join(path_patterns, "*.yml"))}
    # filter patterns not enabled
    patterns = {k: v for k, v in patterns.items() if v.get("enabled", False)}

    if len(patterns) == 0:
        log.error("There aren't logs to generate. Check pattern files")
        return 0

    log.info(f"Loading {len(patterns)} log patterns")

    # calculate max concurrent threads
    concur_req = int(min(MAX_CONCUR_REQ, len(patterns), max_concur_req))

    log.info(f"Activate {concur_req} parallel threads")

    with futures.ThreadPoolExecutor(max_workers=concur_req) as executor:
        res = executor.map(log_generator, patterns.values())
        return sum(res)
