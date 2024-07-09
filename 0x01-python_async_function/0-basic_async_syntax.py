#!/usr/bin/env python3
"""Python async"""

import asyncio
import random
import time


async def wait_random(max_delay: int = 10) -> float:
    """Wait random"""
    s = time.perf_counter()
    await asyncio.sleep(random.randint(0, max_delay))
    res = time.perf_counter() - s
    return res
