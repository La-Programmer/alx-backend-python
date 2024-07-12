#!/usr/bin/env python3
"""Measure runtime"""

import asyncio
import time
from typing import List
wait_n: List[float] = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the runtime of a function"""
    start_time: float = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed_time: float = time.perf_counter() - start_time
    result: float = elapsed_time / n
    return result
