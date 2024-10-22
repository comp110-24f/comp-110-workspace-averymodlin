"""find_max file of cq07"""

__author__ = "730765631"


def find_and_remove_max(nums: list[int]) -> int:
    """this function removes all instances of the largest number from the list"""
    if not nums:  # if no numbers input, return -1
        return -1
    else:
        max_value = max(nums)  # Find the maximum value in the list

        # Remove all instances of the maximum value using a while loop
        while max_value in nums:
            nums.remove(max_value)

        return max_value
