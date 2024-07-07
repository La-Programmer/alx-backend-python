#!/usr/bin/env python3
"""SUM LIST"""


type Vector = list[float]


def sum_list(input_list: Vector):
    """Sum list"""
    accumulator: float = 0.0
    for i in input_list:
        accumulator += i
    return accumulator
