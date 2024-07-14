#!/usr/bin/env python3
"""ASYNC COMPREHENSION"""

import asyncio
from typing import List
from typing import AsyncGenerator
async_generator: AsyncGenerator[int, None]
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Async comprehension"""
    result: List[float] = [i async for i in async_generator()]
    return result
