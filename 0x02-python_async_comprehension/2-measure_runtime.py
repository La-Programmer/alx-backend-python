#!/usr/bin/env python3
"""MEASURE RUNTIME"""

import asyncio
import time
from typing import List
async_comprehension: List[float]
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure runtime"""
    start_time: float = time.perf_counter()
    await asyncio.gather(async_comprehension())
    elapsed_time: float = time.perf_counter() - start_time
    return elapsed_time
