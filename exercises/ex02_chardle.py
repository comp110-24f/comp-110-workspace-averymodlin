"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730765631"

import sys


def input_word() -> str:
    """This gathers input from by asking them the user to input a 5 letter word."""
    user_input = input("Enter a 5-character word: ")
    if len(user_input) != 5:  # if the word isn't exactly 5 letters an error will arise
        print("Error: Word must contain 5 characters.")
        sys.exit()
    else:
        return user_input  # returns the input back if it was an accepted input


def input_letter() -> str:
    """This function asks the user to input a single letter"""
    user_input = input("Enter a single character: ")
    if len(user_input) != 1:  # an error is shown if more than a single letter is input
        print("Error: Character must be a single character.")
        sys.exit()
    return user_input


def contains_char(word: str, letter: str) -> None:
    """checks the word input for the letter input by the user"""
    print(f"Searching for {letter} in {word}")
    found_count = (
        0  # found count must start at 0 because we haven't counted any letters yet
    )

    # Check each index of the word for the letter input
    for index in range(len(word)):
        if word[index] == letter:
            print(f"{letter} found at index {index}")
            found_count += 1
    if found_count == 0:
        print(f"No instances of {letter} found in {word}")
    elif found_count == 1:
        print(f"1 instance of {letter} found in {word}")
    else:  # else meaning that the found count is neither 0 or 1
        print(f"{found_count} instances of {letter} found in {word}")


def main() -> None:
    """The main function to bring the whole game together"""
    word = input_word()  # gets a valid word input from user
    letter = input_letter()  # gets a valid character input from user
    contains_char(
        word, letter
    )  # takes the character and checks the amount of times it is used in the word


if __name__ == "__main__":
    main()
