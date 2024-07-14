#!/usr/bin/env python3
"""ASYNC GENERATOR"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[int, None]:
    """Async generator function"""
    for i in range(10):
        i: int
        await asyncio.sleep(1)
        random_result: Generator[int, None] = random.uniform(0, 10)
        yield random_result
