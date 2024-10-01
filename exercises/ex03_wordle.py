""" creating our own wordle game"""

__author__ = "730765631"


def input_guess(secret_word_len: int) -> str:
    """this function asks the user to guess a word with a specific character length."""
    guess = input(f"Enter a {secret_word_len} character word: ")
    while len(guess) != secret_word_len:
        print(f"That wasn't {secret_word_len} chars! Try again:")
        guess = input(f"Enter a {secret_word_len} character word: ")
    return guess


def contains_char(word: str, char: str) -> bool:
    """this function returns true or false by iterating through the characters in a word."""
    assert len(char) == 1  # Ensure char is a single character
    index = 0
    while index < len(word):
        if word[index] == char:  # if the index of the word matches the char return turn
            return True
        index += 1  # continue the loop by adding 1 to the index
    return False  # if the char is more than the len of the word return false


def emojified(guess: str, secret: str) -> str:
    """This function shows wehether the characters match the characters in the word"""
    assert len(guess) == len(
        secret
    )  # the len of the guess word and the length of the secret word

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    emoji_string = ""
    index = 0
    while index < len(guess):
        if guess[index] == secret[index]:
            emoji_string += GREEN_BOX  # correct letter and index
        elif contains_char(secret, guess[index]):
            emoji_string += YELLOW_BOX  # correct Letter but in the wrong index
        else:
            emoji_string += WHITE_BOX  # not a letter in the word
        index += 1

    return emoji_string


def main(secret: str) -> None:
    """main loop of the program that adds the functions and makes them work together"""
    turns = 6
    current_turn = 1
    while (
        current_turn <= turns
    ):  # while you have less than or equal to 6 turns it'll prompt for another guess
        print(f"=== Turn {current_turn}/{turns} ===")
        guess = input_guess(len(secret))
        emoji_result = emojified(guess, secret)
        print(emoji_result)

        if guess == secret:
            print(f"You won in {current_turn}/{turns} turns!")
            return

        current_turn += 1
    print(f"X/{turns}- Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes)")  # you can put any word in place of codes!
