#!/usr/bin/env python3
'''Async Generator'''
import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''Async Generator'''
    result: List[float] = []
    async for i in async_generator():
        result.append(i)
    return result
