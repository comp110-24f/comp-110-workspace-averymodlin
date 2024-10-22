"""utils file of the ex05 folder to implement more list unility functions"""

__author__ = "730765631"


def only_evens(input_list: list[int]) -> list[int]:
    """Return a new list containing only even values of the input list."""
    even_list = []
    for item in input_list:
        if item % 2 == 0:
            even_list.append(
                item
            )  # add each item this is true for to the local variable
    return even_list  # since this is local variable it will return only values added to even list


def sub(input_list: list[int], start: int, end: int) -> list[int]:
    """Return a subset of the input list from start index to end index (exclusive)."""
    if len(input_list) == 0 or start >= len(input_list) or end <= 0:
        return []  # returns an empty list

    if start < 0:  # if the start is a negative then start at 0
        start = 0
    if end > len(
        input_list
    ):  # if the end is larger than the len of the list then the end is the len
        end = len(input_list)

    subset = []
    for index in range(start, end):
        subset.append(input_list[index])
    return subset


def add_at_index(input_list: list[int], element: int, index: int) -> None:
    """Append an element at the specific index in input list."""
    if index < 0 or index > len(
        input_list
    ):  # index must be greater than 0, or less than len of list
        raise IndexError("Index is out of bounds for the input list")

    input_list.append(0)
    for i in range(
        len(input_list) - 1, index, -1
    ):  # because len and index can be the same but len doesn't count from 0
        input_list[i] = input_list[i - 1]  # Shift elements to the right
    input_list[index] = element  # insert the new element at appropriate index
