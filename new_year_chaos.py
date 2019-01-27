#!/bin/python3
# See https://www.hackerrank.com/challenges/new-year-chaos/problem

import math
import os
import random
import re
import sys

# Reengineered, somewhat, but TC 7 still times out. Expected value is:
# 115173
# Too chaotic
# 115013
# Too chaotic

# We should sort this as little as possible; since it begins life as a range and we remove items
# as we consume them. (Since replaced by sorted_census.)
# sorted_q = None

def minimumBribes(q):
    sorted_census = list(range(1, len(q) + 1))
    # if test_for_chaos(q):
    #     print("Too chaotic")
    #     return "CHAOS!"
    score = 0
    for ix, original_tag in enumerate(q):
        score += sorted_census.index(original_tag)
        sorted_census.remove(original_tag)

    # rv = minimumBribes_impl(q, 0)
    print(score)
    return score


## Let's try some pseudocode.
# 2,1,5,3,4
# First iteration: 2. 2 is not 1, so add (2-1) to the score. Remove 2 from our sorted census and
# adjust expectations. (No longer normalize... based expectations on the sorted census.
# Second iteration: 1. 1 is the lowest number left in the census. Leave the score as is and
# remove 1 from the census.
# Third: 5. This is the 3rd-lowest in the census. add (3-1) to the score and remove 5.

def minimumBribes_impl(q, subtotal):
    # iterator = enumerate(q)
    # for ix, item in enumerate(q):
    #     print(ix)
    #     print(item)
    global sorted_q
    lookup_table = list(sorted_q)
    for ix, original_tag in enumerate(q):
        # The right side of this should not be original any more. It seems like it should be
        # sorted_q[ix-1]. In fact the for loop doesn't really make sense I don't think.

        # What we want to do is say, "Are you the lowest (or 2nd lowest etc) one left?
        # Are you in the correct position for that? Great!
        if original_tag == sorted_q.index(original_tag) + 1:
            sorted_q.remove(original_tag)
            continue
        # Eventually rather than a separate test_for_chaos we could test here, probably.
        sorted_q.remove(original)
        #### normalized = normalize(q[ix:])

        #This implementation still feels like it's doing extra work. The notion is,
        # now that we've normalized q for the next recursion, we reset the (smaller) sorted
        # list to match, which means just the (smaller) range of numbers.
        #### sorted_q = list(range(1, len(q) + 1))
        return minimumBribes_impl(q[ix:], subtotal + (original - ix))
    return subtotal

def normalize(q):
    global sorted_q
    rv = []
    # sorted_q = sorted(q)
    # Possible list comprehension
    for item in q:
        rv.append(sorted_q.index(item)+1)
    return rv

def test_for_chaos(q):
    is_chaotic = any([(original - ix - 1 > 2) for ix, original in enumerate(q)])
    if (is_chaotic):
        return True

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

    # arr = [1, 2, 5, 3, 7, 8, 6, 4,]
    # minimumBribes(arr)
    harness()
    exit()

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)

