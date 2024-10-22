"""max_test file of cq07"""

__author__ = "730765631"

import unittest
from find_max import find_and_remove_max


class TestFindAndRemoveMax(unittest.TestCase):

    def test_return_value(self) -> None:  # Test that it returns the expected max value
        """returns the expected value"""
        self.assertEqual(find_and_remove_max([1, 2, 3, 4, 5]), 5)

    def test_mutation_input(
        self,
    ) -> None:  # Test that the input list is mutated correctly
        """mutates the imput in the expected way"""
        nums = [1, 5, 3, 5, 2]
        result = find_and_remove_max(nums)
        self.assertEqual(result, 5)
        self.assertEqual(nums, [1, 3, 2])  # 5 should be removed

    def test_single_value(self) -> None:  # Test with a single value in the list
        """returns the correct value in case of an unconvential input"""
        nums = [8]
        result = find_and_remove_max(nums)
        self.assertEqual(result, 8)
        self.assertEqual(nums, [])  # List should be empty afterwards
