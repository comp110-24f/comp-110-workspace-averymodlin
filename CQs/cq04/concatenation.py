"""The concatenation file of cq04 provides the function concat which concatenates two strings"""

__author__ = "730765631"


def concat(str_1: str, str_2: str) -> str:
    """concatenate two strings"""
    return str_1 + str_2


word1: str = "happy"
word2: str = "tuesday"

if __name__ == "__main__":
    print(concat(word1, word2))
