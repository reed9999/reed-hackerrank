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
# It's saying both testcases
# are too chaotic.
def minimumBribes(q):
    is_chaotic = any([(original - ix - 1 > 2 ) for ix, original in enumerate(q)])
    rv = sum([(original - ix - 1) for ix, original in enumerate(q) if original > ix + 1])
    if (is_chaotic):
        print ("Too chaotic")
        return "CHAOS"
    else:
        print(rv)
        return rv

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
