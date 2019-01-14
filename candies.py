#!/bin/python3

import math
import os
import random
import re
import sys


##
# Currently I'm using the brute force approach below. This seems to give right answers, but it
# has a ridiculous amount of rework and other inefficiencies.

# It might have been simpler just to
# 1. find the minimum score and assign it 1
# 2. assign the neighbors 2.
# 3. adjust those neighbors/their second-order neighbors as I'm doing here, incrementing as needed.
# 4. Etc

# Note that test case 14 should return: 204867
# This one does take at least 5 minutes to run on my comp using the brute force approach, so
# it's reasonable that it times out on their server.

# The brute force method
def local_minima_approach(lscores):
    #See https://www.hackerrank.com/challenges/candies/forum/comments/347497
    # But how does it deal with the tiebreakers?
    raise NotImplementedError

    list_of_lists = []
    current = []
    for i in range(lscores):
        if (i==0 and lscores[0] < lscores[1]) or \
                (i == len(iscores)-1 and lscores[i] < lscores[i-1]):
            current.append(i)
        if (lscores[i] < lscores [i-1] and lscores[i] < lscores[i+1]):
            current.append(i)
    list_of_lists.append(current)


#Copy paste not yet edited.
    for i in range(lscores):
        if (i== len(iscores)-1 and lscores[i] < lscores[i-1]):
            current.append(i)
        if (lscores[i] < lscores [i-1] and lscores[i] < lscores[i+1]):
            current.append(i)
    list_of_lists.append(current)


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
    if len(rv) % 200 == 0:
        print("Pass with {} violations".format(len(rv)))
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
    # rv = brute_force_approach(arr, lcandies,)
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
