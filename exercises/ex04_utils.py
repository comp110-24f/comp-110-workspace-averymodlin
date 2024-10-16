"""ex04_utils """

__author__ = "730765621"


def all(input_list: list[int], value: int) -> bool:
    """this function will return true if the values in the list match the input values, if not False"""
    if len(input_list) == 0:
        return False  # zero input is false
    for item in input_list:
        if item != value:
            return False  # Return False if any item is not equal to value
    return True  # Return True if all items are equal to value


def max(input_list: list[int]) -> int:
    """This function returns the maximum integer in a list or raisees ValueError if the list is empty.."""
    if len(input_list) == 0:
        raise ValueError("max() arg is an empty List")

    max_value = input_list[
        0
    ]  # first number is the max, because this is how we compare it to the others
    for item in input_list:
        if item > max_value:
            max_value = item  # change max_value if a larger number is found
    return max_value


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Return True if both lists are equal in values at each index, if not return false"""
    if len(list_1) != len(list_2):
        return False  # If lengths are different then the lists can't be equal

    for index in range(len(list_1)):
        if list_1[index] != list_2[index]:
            return False  # Return False if any of the indexes of each list aren't equal
    return True  # Return True if all corresponding indexes are equal


def extend(list_1: list[int], list_2: list[int]) -> None:
    """mutate list_1 by appending the elements from list_2 to the end of list_1"""
    for item in list_2:
        list_1.append(item)  # append each item from list_2 to list_1
