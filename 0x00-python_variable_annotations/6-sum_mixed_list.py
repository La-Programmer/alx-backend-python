#!/usr/bin/env python3
"""SUM MIXED LIST"""


type Vector = list[float | int]


def sum_mixed_list(mxd_lst: Vector) -> float:
    """Sum a mixed list"""
    accumulator: float = 0
    for i in mxd_lst:
        accumulator += float(i)
    return accumulator
