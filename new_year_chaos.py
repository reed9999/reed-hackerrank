#!/bin/python3
# See https://www.hackerrank.com/challenges/new-year-chaos/problem

import math
import os
import random
import re
import sys

# It's saying both testcases
# are too chaotic.
def minimumBribes(q):
    is_chaotic = any([(original - ix > 2) for ix, original in enumerate(q)])
    rv = sum([abs(ix - original) for ix, original in enumerate(q)])
    if (is_chaotic):
        print ("Too chaotic")
        print ([(original - ix > 2) for ix, original in enumerate(q)])
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
