#!/usr/bin/env python3
"""Concurrent coroutines"""

import asyncio
from typing import List
task_wait_random: asyncio.Task = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Runs multiple coroutines concurrently"""
    tasks: List[asyncio.Task] = [task_wait_random(max_delay) for i in range(n)]
    res: List[float] = []
    for task in asyncio.as_completed(tasks):
        task: asyncio.Task
        result: float = await task
        res.append(result)
    return res
