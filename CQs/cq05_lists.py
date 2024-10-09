"""Mutating functions."""

__author__ = "730765631"


def manual_append(a: list[int], value: int) -> None:
    """This function takes the input and appends it to the end of list a"""
    a.append(value)  # add (append) the value inputted to the end of the list


def double(a: list[int]) -> None:
    """Mutates inputs by looping through the list and multiplying every value by the paramater 2"""
    index: int = 0
    while index < len(a):  # while index is less than or equal to the length of list a
        a[index] *= 2  # double each index element
        index += 1  # index plus 1 to move through each index


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)
print(list_1)
print(list_2)
