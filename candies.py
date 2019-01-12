#!/bin/python3

import math
import os
import random
import re
import sys

def compare_min_scores(x, y):
    min_x = min(x)
    min_y = min(y)
    the_min = min(min_x, min_y)
    if min_x == the_min:
        if min_y == the_min:
            return 0
        else:
            return -1
    else:
        return 1

def adjust_candies(scores, candies):
    xsc, ysc = scores[0], scores[1]
    xcan, ycan = candies[0], candies[1]
    if xsc > ysc:
        xcan = max (xcan, ycan + 1)
    elif ysc > xsc:
        ycan = max (ycan, xcan + 1)
    # I thought we could do operations directly on the slice...
    candies[0], candies[1] = xcan, ycan
    # ... but that may be my overreliance on pandas slices. :)
    # Instead use the returned value.
    return (xcan, ycan)


def candies_impl(arr, candies_slice):
    n = len(arr)
    if n == 1:
        return candies_slice[0]
    # elif n == 2:
    #     x = arr[0]
    #     y = arr[1]
    #     adjust_candies((x, y), (candies_arr[0], candies_arr[1]))
    #     return sum(candies_arr)
    else:
        # pick a len roughly at the midpoint. It shouldn't matter if it's exactly the midpoint as long as
        # each side has at least one element.
        i = int( n / 2 )
        left = arr[:i]
        right = arr[i:]
        new_candy_counts = adjust_candies(arr[i-1:i+1], candies_slice[i-1:i+1])
        # Note that we can change candies_array directly by changing values in the slice.
        candies_slice[i-1], candies_slice[i] = new_candy_counts
        return candies_impl(left, candies_slice[:i]) + candies_impl(right, candies_slice[i:])

def candies(n, arr):
    assert n == len(arr)
    global candies_arr
    candies_arr = [1] * n
    rv = candies_impl(arr, candies_arr)
    assert rv == sum(candies_arr)
    return rv

def harness():
    assert 6 == candies(3, [4, 5, 6])
    assert 3 == candies(2, [4, 5])
    assert (2, 1) == adjust_candies((5, 4), (1, 1))
    assert (17, 2) == adjust_candies((4, 4), (17, 2))
    assert (17, 18) == adjust_candies((4, 5), (17, 2))
    assert (17, 17) != adjust_candies((4, 5), (17, 2))
if __name__ == '__main__':
    harness()
    exit()
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
