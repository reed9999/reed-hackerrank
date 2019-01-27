#!/bin/python3
# See https://www.hackerrank.com/challenges/new-year-chaos/problem

import math
import os
import random
import re
import sys

# This version passes all tests. For the record expected value for TC7 is:
# 115173
# Too chaotic
# 115013
# Too chaotic

def minimumBribes(q):
    sorted_census = list(range(1, len(q) + 1))
    score = 0
    for ix, original_tag in enumerate(q):
        sorted_index = sorted_census.index(original_tag)
        if sorted_index > 2:
            print("Too chaotic")
            return "CHAOS!"

        score += sorted_census.index(original_tag)
        sorted_census.remove(original_tag)

    # rv = minimumBribes_impl(q, 0)
    print(score)
    return score


## Here's the pseudocode that broke me out of complicating this problem unnecessarily. :)
# 2,1,5,3,4
# First iteration: 2. 2 is not 1, so add (2-1) to the score. Remove 2 from our sorted census and
# adjust expectations. (No longer normalize... based expectations on the sorted census.
# Second iteration: 1. 1 is the lowest number left in the census. Leave the score as is and
# remove 1 from the census.
# Third: 5. This is the 3rd-lowest in the census. add (3-1) to the score and remove 5.

### PASTEIN TO HACKERRANK SHOULD END HERE



def harness():
    input = """2
5
2 1 5 3 4
5
2 5 1 3 4""".splitlines()
    input = iter(input)
    expected_values = iter([3, "CHAOS!"])
    t = int(next(input))

    for t_itr in range(t):
        n = int(next(input))

        q = list(map(int, next(input).rstrip().split()))
        print (q)
        ev = next(expected_values)
        assert ev == minimumBribes(q)


if __name__ == '__main__':

    arr = [1, 2, 5, 3, 7, 8, 6, 4,]
    minimumBribes(arr)
    harness()
    exit()

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)

