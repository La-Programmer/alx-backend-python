#!/usr/bin/env python3
"""Concurrent Coroutines"""

import asyncio
from typing import List
wait_random: float = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Runs multiple coroutines concurrently"""
    tasks: List[asyncio.Task] = [wait_random(max_delay) for i in range(n)]
    res: List[float] = []
    for task in asyncio.as_completed(tasks):
        task: asyncio.Task
        result: float = await task
        res.append(result)
    return res
