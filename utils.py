
import re
from itertools import combinations, permutations, combinations_with_replacement
from collections import Counter




class ALPHA:
    vowels = "aeiou"
    VOWELS = vowels.upper()
    alpha = "abcdefghijklmnopqrstuvwxyz"
    ALPHA = alpha.upper()



def groups(it, gsize, overlap=False):

    return [it[i:i+gsize] for i in range(0, len(it), 1 if overlap else gsize)]


def count_all(iter, targ):
    t = 0
    for it in iter:
        if it in targ:
            t += 1
    return t

def lmi(d):
    return list(map(int, d))

def sum_pos(pos1, pos2):
    assert len(pos1) == len(pos2)
    return [pos1[i]+pos2[i] for i in range(len(pos1))]

class ADJ4:
    ADJ4 = [(0,1), (1,0), (0,-1), (-1,0)] # (x,y) Clockwise from north of compass
    inputs = [
        "^>v<",
        "nesw",
        "NESW",

    ]

    LOOK = {}
    for inp in inputs:
        LOOK |= dict(zip(inp, ADJ4))
    print(LOOK)