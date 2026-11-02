#!/usr/bin/env python3
"""Measure the total runtime of four parallel async comprehensions."""

import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Run async_comprehension four times concurrently with asyncio.gather
    and return the total elapsed time in seconds."""

    start = time.perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )
    end = time.perf_counter()

    return end - start
