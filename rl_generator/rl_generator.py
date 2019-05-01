# -*- coding: utf-8 -*-

"""Main module."""

import time
from tqdm import tqdm


def log_generator(pattern_conf):
    pass


def test(eps=10, time_period=10):
    nr_logs = eps * time_period
    sleep_time = 1 / eps
    print(sleep_time)
    for j in tqdm(range(10)):
        for i in tqdm(range(nr_logs)):
            # print(str(time.time()) + f" {i}")
            # print(f"{time.time()} {i}")
            time.sleep(sleep_time)
