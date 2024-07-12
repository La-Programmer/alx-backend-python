#!/usr/bin/env python3
"""Task"""

import asyncio
wait_random: float = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Task wait random"""
    task: asyncio.Task = asyncio.create_task(wait_random(max_delay))
    return task
