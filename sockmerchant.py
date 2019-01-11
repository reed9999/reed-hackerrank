#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

def tally_of_counts(counts):
    total = 0
    for k in counts.keys():
        total += int(counts[k] / 2.0)
    return total

def sockMerchant_naive(n, ar):
    counts = {}
    for sock in ar:
        if sock in counts.keys():
            counts[sock] += 1
        else:
            counts[sock] = 1
    return tally_of_counts(counts)

def sockMerchant(n, ar):
    # return sockMerchant_naive(n, ar)
    the_counter = Counter(ar)
    return tally_of_counts(the_counter)



def test_harness():
    assert 0 == sockMerchant(0, []), "one"
    assert 0 == sockMerchant(1, [99,]), "two"
    assert 1 == sockMerchant(1, [7, 7,]), "three"
    assert 5 == sockMerchant(1, [3, 4, 5, 3, 6, 5, 3, 3, 5, 7, 4,]), "four"
if __name__ == '__main__':
    test_harness()
if __name__ == None:
    print ("choke")
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
