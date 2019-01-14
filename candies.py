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

#
# def adjust_candies(scores, candies):
#     xsc, ysc = scores[0], scores[1]
#     xcan, ycan = candies[0], candies[1]
#     if xsc > ysc:
#         xcan = max (xcan, ycan + 1)
#     elif ysc > xsc:
#         ycan = max (ycan, xcan + 1)
#     # I thought we could do operations directly on the slice...
#     candies[0], candies[1] = xcan, ycan
#     # ... but that may be my overreliance on pandas slices. :)
#     # Instead use the returned value.
#     return (xcan, ycan)
#
#
# def candies_impl(lscores, lcandies, rangespec):
#     start, stop = rangespec[0], rangespec[1]
#     n = stop - start
#     if n == 1:
#         return lcandies[start]
#     else:
#         # pick a len roughly at the midpoint. It shouldn't matter if it's exactly the midpoint as long as
#         # each side has at least one element.
#         i = int( n / 2 )
#         pivot = start + i   #index of the first element of the right side
#         left_result = candies_impl(lscores, lcandies, [start, pivot])
#         right_result = candies_impl(lscores, lcandies, [pivot, stop])
#         new_candy_counts = adjust_candies(lscores[pivot-1 : pivot+1], lcandies[pivot-1 : pivot+1])
#         lcandies[pivot-1] = new_candy_counts[0]
#         lcandies[pivot] = new_candy_counts[1]
#
#         # It feels like we should do the recursive calls again (now that we've situated the boundary counts) but
#         # that also seems incredibly inefficient.
#         # return  left_result + right_result
#         return  sum(lcandies[start:stop])




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

def simple_attempt(lscores, lcandies):
    # Not my solution. See https://www.hackerrank.com/challenges/candies/forum/comments/81516
    # but test case 2 in the hidden suite gives 35197 whereas correct is 42105
    assert(len(lscores) == len(lcandies))
    for i in range(1, len(lscores)):
        if lscores[i] > lscores [i-1]:
            lcandies[i] = max(lcandies[i], lcandies[i-1] + 1)
    for i in range(len(lscores)-1, -1):
        if lscores[i] > lscores [i+1]:
            lcandies[i] = max(lcandies[i], lcandies[i+1] + 1)
    return sum(lcandies)

def find_all_violations(lscores, lcandies):
    assert(len(lscores) == len(lcandies))
    rv = []
    lstudents = zip(range(len(lscores)), iter(lscores), iter(lcandies))
    (i, last_score, last_candies) = next(lstudents)
    for (i, score, candies) in lstudents:
        if score > last_score and last_candies >= candies:
            rv.append((i, True))
        elif score < last_score and last_candies <= candies:
            rv.append((i-1, False))
        last_score, last_candies = score, candies
    return rv

def violation_to_fix(lscores, lcandies, vios):
    #First cut: Pick one at random!
    # return random.choice(vios)
    #Second cut: Always the first!
    return vios[0]

def fix(lscores, lcandies, curr_vio,):
    higher_score_ix, is_left = curr_vio
    lower_score_candies = lcandies[higher_score_ix + (-1 if is_left else +1)]
    lcandies[higher_score_ix] = 1 + lower_score_candies


def brute_force_approach(lscores, lcandies,):
    while True:
        vios = find_all_violations(lscores, lcandies)
        if len(vios) <= 0:
            return sum(lcandies)
        curr_vio = violation_to_fix(lscores, lcandies, vios,)
        fix(lscores, lcandies, curr_vio,)
    return None


def candies(n, arr):
    assert n == len(arr)
    lcandies = [1] * n
    # rv = candies_impl(arr, lcandies, [0, n])
    rv = brute_force_approach(arr, lcandies,)
    assert rv == sum(lcandies)
    return rv

def harness():
    tc1 = [2, 4, 2, 6, 1, 7, 8, 9, 2, 1]
    assert 19 == candies(10, tc1)
    assert 4 == candies(3, [99, 99, 98]) #counterintuitive but [1, 2, 1] is acceptable because of the tie score.
    assert 6 == candies(3, [4, 5, 6])
    assert 4 == candies(3, [4, 6, 5])
    assert 3 == candies(3, [99, 99, 99])
    assert 3 == candies(2, [4, 5])
    # assert (2, 1) == adjust_candies([5, 4,], [1, 1,])
    # assert (17, 2) == adjust_candies([4, 4,], [17, 2,])
    # assert (17, 18) == adjust_candies([4, 5,], [17, 2,])
    # assert (17, 17) != adjust_candies([4, 5,], [17, 2,])
if __name__ == '__main__':
    # harness();    exit()
    os.environ['OUTPUT_PATH'] = 'temp.txt'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
