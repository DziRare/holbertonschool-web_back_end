#!/usr/bin/env python3
"""This module is for async comprehension and genertation"""

from typing import AsyncGenerator

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> AsyncGenerator[float, None, None]:
    """This function is for async comprehension and genertation"""

    return [num async for num in async_generator()]
