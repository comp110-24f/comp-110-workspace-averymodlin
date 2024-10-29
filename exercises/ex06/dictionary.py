"""in this exercise we will practice with dictionary functions"""

__author__ = "730765631"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """takes a dictionary and makes the keys the values and vice versa"""
    inverted_dict = {}  # create an empty list that the inverted list will be in

    for (
        key,
        value,
    ) in input_dict.items():  # iterates over key-value pairs of the input dict
        if value in inverted_dict:
            raise KeyError(
                f"Duplicate value found: '{value}'"
            )  # if a value was input twice it'll raise a key error when inverting dict
        inverted_dict[value] = (
            key  # the value of the input is now the key value in the invert dict
        )

    return inverted_dict  # return invert dictionary


def favorite_color(colors_dict: dict[str, str]) -> str:
    """function takes a dictionary and returns the color input in most"""
    color_count: dict[str, int] = {}  # a new dictionary to keep track of color count

    # Count the occurrences of each color
    for color in colors_dict.values():
        if color in color_count:
            color_count[color] += 1  # add to the color count
        else:
            color_count[color] = 1  # leave the color count at 1

    most_frequent_color: str = ""
    max_count: int = 0

    for (
        color
    ) in colors_dict.values():  # iterate through each color count to find the highest
        count = color_count[color]
        if count > max_count:
            max_count = count
            most_frequent_color = color

    return most_frequent_color


def count(values: list[str]) -> dict[str, int]:
    """produces a dict where each key is a value, each value is a count of it in list"""
    result: dict[str, int] = {}
    for item in values:
        if (
            item in result
        ):  # Check if the item is already a key in the result dictionary
            result[item] += 1  # add one to the count
        else:
            result[item] = 1  # start the count for the item

    return result


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """produce dict with key where the values are words beginning with same letter"""
    result: dict[str, list[str]] = {}
    for word in words:  # Loop through each word in the input list
        first_letter = word[
            0
        ].lower()  # Converts the first letter of the words to lowercase

        if first_letter not in result:  # Initialize the key if it doesn't exist
            result[first_letter] = []

        result[first_letter].append(word)  # Append the word to the corresponding list

    return result


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    """mutates dict to return the new attendance information"""
    if day not in attendance:  # makes sure all days are added as a key
        attendance[day] = []

    if student not in attendance[day]:
        attendance[day].append(student)  # if the student isn't already then add them
