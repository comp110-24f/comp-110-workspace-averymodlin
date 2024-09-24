__author__ = "730765631"


def num_instances(phrase: str, search_char: str) -> None:
    # this function evalutes the number of times a charcter is repeated in a phrase
    count = 0
    index = 0

    while index < len(phrase):
        # if the current character matches search_char
        if phrase[index] == search_char:
            count += 1
        # add 1 to move to the next character of the phrase
        index += 1
