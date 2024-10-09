"""Summing the elements of a list using different loops"""

__author__ = "730765631"


def w_sum(vals: list[float]) -> float:
    """this function uses the while loop to sum each value in the vals list"""
    total: float = 0.0
    idx: int = 0
    while idx < len(vals):  # while the idx is less than the len of vals
        total += vals[idx]  # add each index to the total
        idx += 1
    return total


def f_sum(vals: list[float]) -> float:
    """This function uses the for...in loop to sum the vals in the vals list"""
    total = 0.0
    for value in vals:  # for each value in vals add it to the total
        total += value
    return total


def f_range_sum(vals: list[float]) -> float:
    """this function uses the in range loop to sum the values of the vals list"""
    total = 0.0
    for index in range(
        len(vals)
    ):  # for each index in the range of the len of the vals list add it to total
        total += vals[index]
    return total
