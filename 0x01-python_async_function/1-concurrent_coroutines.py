#!/usr/bin/env python3
"""Concurrent Coroutines"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> 'list[float]':
    """Runs multiple coroutines concurrently"""
    tasks = [wait_random(max_delay) for i in range(n)]
    res = []
    for task in asyncio.as_completed(tasks):
        result = await task
        res.append(result)
    return res
