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
    xsc, ysc = scores
    xcan, ycan = candies
    if xsc > ysc:
        xcan = max (xcan, ycan + 1)
    elif ysc > xsc:
        ycan = max (ycan, xcan + 1)
    return (xcan, ycan)


def candies(n, arr):
    candies_arr = [0] * n
    if n == 2:
        x = arr[0]
        y = arr[1]
        adjust_candies((x, y), (candies_arr[0], candies_arr[1]))
        return sum(candies_arr)
    else:
        # pick a len roughly at the midpoint. It shouldn't matter if it's exactly the midpoint.
        i = int( n / 2 )
        left = arr[:i+1]
        right = arr[i+1:]
        # This is buggy -- we need to assess the point of connection between them for rules violations
        return candies(i, left) + candies(n - i, right)


def harness():
    assert (2, 1) == adjust_candies((5, 4), (1, 1))
    assert (17, 2) == adjust_candies((4, 4), (17, 2))
    assert (17, 18) == adjust_candies((4, 5), (17, 2))
    assert (17, 17) != adjust_candies((4, 5), (17, 2))
    assert 9999 != candies(3, [4, 5, 6])
    assert 3 == candies(2, [4, 5])
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
