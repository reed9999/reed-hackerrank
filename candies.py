#!/bin/python3

import math
import os
import random
import re
import sys

## The assumptions of my algorithm are pretty wrong (in particular, when you adjust on the boundary between
# right and left, you need to propagate that adjustment through as needed) but it might have been simpler just to
# 1. find the minimum score and assign it 1
# 2. assign the neighbors 2.
# 3. adjust those neighbors/their second-order neighbors as I'm doing here, incrementing as needed.
# 4. Etc
# but you still need to propagate somehow.


candies_array = None
# def compare_min_scores(x, y):
#     min_x = min(x)
#     min_y = min(y)
#     the_min = min(min_x, min_y)
#     if min_x == the_min:
#         if min_y == the_min:
#             return 0
#         else:
#             return -1
#     else:
#         return 1

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


def candies_impl(lscores, lcandies, rangespec):
    start, stop = rangespec[0], rangespec[1]
    n = stop - start
    if n == 1:
        return lcandies[start]
    else:
        # pick a len roughly at the midpoint. It shouldn't matter if it's exactly the midpoint as long as
        # each side has at least one element.
        i = int( n / 2 )
        pivot = start + i   #index of the first element of the right side
        left_result = candies_impl(lscores, lcandies, [start, pivot])
        right_result = candies_impl(lscores, lcandies, [pivot, stop])
        new_candy_counts = adjust_candies(lscores[pivot-1 : pivot+1], lcandies[pivot-1 : pivot+1])
        lcandies[pivot-1] = new_candy_counts[0]
        lcandies[pivot] = new_candy_counts[1]

        # It feels like we should do the recursive calls again (now that we've situated the boundary counts) but
        # that also seems incredibly inefficient.
        # return  left_result + right_result
        return  sum(lcandies[start:stop])

def candies(n, arr):
    assert n == len(arr)
    candies_arr = [1] * n
    rv = candies_impl(arr, candies_arr, [0, n])
    # Weirdly in the basic three-student case rv is turning out OK but candies_arr is butchered.
    # I doubt this is sustainable but let's see!
    assert rv == sum(candies_arr)
    return rv

def harness():
    tc1 = [2, 4, 2, 6, 1, 7, 8, 9, 2, 1]
    assert 19 == candies(10, tc1)
    assert 4 == candies(3, [99, 99, 98]) #counterintuitive but [1, 2, 1] is acceptable because of the tie score.
    assert 6 == candies(3, [4, 5, 6])
    assert 4 == candies(3, [4, 6, 5])
    assert 3 == candies(3, [99, 99, 99])
    assert 3 == candies(2, [4, 5])
    assert (2, 1) == adjust_candies([5, 4,], [1, 1,])
    assert (17, 2) == adjust_candies([4, 4,], [17, 2,])
    assert (17, 18) == adjust_candies([4, 5,], [17, 2,])
    assert (17, 17) != adjust_candies([4, 5,], [17, 2,])
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
