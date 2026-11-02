#!/usr/bin/env python3

"""The module is for measuring the total execution time"""

import asyncio
import time

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """This function is measuring the total execution time"""

    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()

    return end - start
