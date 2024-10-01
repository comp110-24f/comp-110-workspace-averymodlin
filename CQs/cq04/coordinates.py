"""The coordinate file of cq04"""

__author__ = "730765631"


def get_coords(xs: str, ys: str) -> None:
    """Prints the formmatted pairs of each character in the two imput strings"""
	index = 0
    while index < len(xs): #iterates over every character in xs
        idx = 0
        while idx < len(ys): #iterates over every character in ys
            print(f"({xs[index]},{ys[idx]}")
			idx += 1
        index += 1

