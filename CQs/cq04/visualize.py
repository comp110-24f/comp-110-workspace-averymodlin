"""Visualize file of cq04, where we have imported functions from other files to call"""

__author__ = "730765631"

from CQs.cq04.concatenation import concat
from CQs.cq04.coordinates import get_coords

x = "123"
y = "abc"

result = concat(x, y)
print(result)

get_coords(x, y)
