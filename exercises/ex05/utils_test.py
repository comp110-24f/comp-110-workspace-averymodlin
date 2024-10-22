"""utils test file of the ex05 folder to define unit tests"""

__author__ = "730765631"

import pytest
from exercises.ex05.utils import only_evens, sub, add_at_index


def test_only_evens_positive_and_negative():
    """Test only_evens with a list of positive and negative numbers."""
    assert only_evens([-3, -2, -1, 0, 1, 2]) == [
        -2,
        0,
        2,
    ]  # removed all non even numbers, negative and positive


def test_only_evens_empty_list():
    """Test only_evens with an empty list."""
    assert only_evens([]) == []  # will return an empty list if given one


def test_only_evens_does_not_mutate_input():
    """Test that only_evens does not mutate the input list."""
    original = [1, 2, 3]  # should not mutate the original
    only_evens(original)
    assert original == [1, 2, 3]


def test_sub_with_valid_indices():
    """Test sub with valid indices."""
    assert sub([10, 20, 30, 40], 1, 3) == [
        20,
        30,
    ]  # returns start and end because end was shorter than len of list


def test_sub_with_negative_start_index():
    """Test sub with negative start index."""
    assert sub([10, 20, 30, 40], -1, 3) == [
        10,
        20,
        30,
    ]  # because it is a negative start start from 0


def test_sub_with_empty_list():
    """Test sub with an empty list."""
    assert (
        sub([], 1, 3) == []
    )  # if start is less than the len of the list return empty, didn't mutate original


def test_add_at_index_inserts_at_middle():
    """Test add_at_index inserts an element at the middle of the list."""
    lst = [1, 2, 4]
    add_at_index(lst, 3, 2)  # append 3 to index 2
    assert lst == [1, 2, 3, 4]


def test_add_at_index_inserts_at_end():
    """Test add_at_index inserts an element at the end of the list."""
    lst = [1, 2, 3]
    add_at_index(
        lst, 4, 3
    )  # adds the value to the end of the list although that index doesn't exist
    assert lst == [1, 2, 3, 4]


def test_add_at_index_raises_indexerror():
    """Test that add_at_index raises an IndexError for an invalid index."""
    with pytest.raises(IndexError):
        add_at_index([], 1, 1)  # if theres no list you can't append values

    with pytest.raises(IndexError):
        add_at_index([1, 2, 3], 4, 5)  # the index is larger then the length of the list
