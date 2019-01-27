#!/bin/python3
# See https://www.hackerrank.com/challenges/new-year-chaos/problem

import math
import os
import random
import re
import sys

# TC 7 times out. Expected value is:
# 115173
# Too chaotic
# 115013
# Too chaotic

sorted_q = None

def minimumBribes(q):
    global sorted_q
    sorted_q = list(range(1, len(q) + 1))
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
            # Sorting at each recursion below was senseless, so this replaces a sort.
            sorted_q.remove(ix)
            continue
        # Eventually rather than a separate test_for_chaos we could test here, probably.
        return minimumBribes_impl(normalize(q[ix:]), subtotal + (original - ix))
    return subtotal

def normalize(q):
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

