#!/bin/python3
# See https://www.hackerrank.com/challenges/new-year-chaos/problem

import math
import os
import random
import re
import sys

"""Key test case
8
1 2 5 3 7 8 6 4
Proceed to the 5 in place 3. That's two bribes so count 2. Normalize the remaining array:
3 7 8 6 4
becomes
1 4 5 3 2
Proceed to 4. Count 2 (4 cumulative) leaving 5 3 2 -> 3 2 1.
Count 2 for the 3 (6 cumul) leaving 2 1 which of course is 1 more.
"""

# TC 7 times out. Expected value is:
# 115173
# Too chaotic
# 115013
# Too chaotic

def minimumBribes(q):
    if test_for_chaos(q):
        print("Too chaotic")
        return "CHAOS!"
     # This might be easier to follow with a list comprehension and/or reduce but it's still pretty
    # straightforward.
    rv = minimumBribes_impl(q, 0)
    print(rv)
    return rv

def minimumBribes_impl(q, subtotal):
    # iterator = enumerate(q)
    # for ix, item in enumerate(q):
    #     print(ix)
    #     print(item)
    for ix, original in enumerate(q):
        ix += 1     #one-based, not zero-based
        if ix == original:
            continue
        # Eventually rather than a separate test_for_chaos we could test here, probably.
        return minimumBribes_impl(normalize(q[ix:]), subtotal + (original - ix))
    return subtotal

def normalize(q):
    rv = []
    sorted_q = sorted(q)
    # Possible list comprehension
    for item in q:
        rv.append(sorted_q.index(item)+1)
    return rv

def test_for_chaos(q):
    is_chaotic = any([(original - ix - 1 > 2) for ix, original in enumerate(q)])
    if (is_chaotic):
        return True

if __name__ == '__main__':
    arr = [1, 2, 5, 3, 7, 8, 6, 4,]
    minimumBribes(arr)
    exit()

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
