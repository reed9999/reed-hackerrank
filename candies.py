#!/bin/python3

import math
import os
import random
import re
import sys


##
# Note that test case 2 should return: 42105
# test case 3 should return: 160929
# test case 14 should return: 204867

# Combining simple attempt with reasonable handling of ties seems to be the winning ticket.

def simple_attempt(lscores,):
    # Based on https://www.hackerrank.com/challenges/candies/forum/comments/81516
    # but there test case 2 in the hidden suite gives 35197 whereas correct is 42105
    # Accounting properly for ties should fix that, maybe?
    n = len(lscores)
    lcandies = [1] * n      #Not really any reason to keep this in the calling code.
    right_partial_answer = 0
    for i in range(1, n):
        if lscores[i] > lscores [i-1]:
            # lcandies[i] = max(lcandies[i], lcandies[i-1] + 1)
            lcandies[i] = lcandies[i-1] + 1
        if lscores[i] == lscores[i - 1]:
            # ties are interesting. Since it doesn't matter how the two compare,
            # we can split the whole thing into a new right-hand piece and recurse.
            n = i
            right_partial_answer = simple_attempt(lscores[i:])
            lscores = lscores[:n]
            lcandies = lcandies[:n]
            break

    for i in range(n-2, -1, -1):
        if lscores[i] > lscores [i+1] and lcandies[i] <= lcandies[i+1]:
            # This time it's important not to change it if it's already correct.
            lcandies[i] = lcandies[i+1] + 1
    return right_partial_answer + sum(lcandies)


# def local_minima_approach(lscores):
#     #See https://www.hackerrank.com/challenges/candies/forum/comments/347497
#     # But how does it deal with the tiebreakers?
#     raise NotImplementedError
#
#     list_of_lists = []
#     current = []
#     for i in range(lscores):
#         if (i==0 and lscores[0] < lscores[1]) or \
#                 (i == len(iscores)-1 and lscores[i] < lscores[i-1]):
#             current.append(i)
#         if (lscores[i] < lscores [i-1] and lscores[i] < lscores[i+1]):
#             current.append(i)
#     list_of_lists.append(current)


#Copy paste not yet edited.
    # for i in range(lscores):
    #     if (i== len(iscores)-1 and lscores[i] < lscores[i-1]):
    #         current.append(i)
    #     if (lscores[i] < lscores [i-1] and lscores[i] < lscores[i+1]):
    #         current.append(i)
    # list_of_lists.append(current)
    #

# def find_all_violations(lscores, lcandies):
#     assert(len(lscores) == len(lcandies))
#     rv = []
#     lstudents = zip(range(len(lscores)), iter(lscores), iter(lcandies))
#     (i, last_score, last_candies) = next(lstudents)
#     for (i, score, candies) in lstudents:
#         if score > last_score and last_candies >= candies:
#             rv.append((i, True))
#         elif score < last_score and last_candies <= candies:
#             rv.append((i-1, False))
#         last_score, last_candies = score, candies
#     # if len(rv) % 200 == 0:
#     #     print("Pass with {} violations".format(len(rv)))
#     return rv
#
# def violation_to_fix(lscores, lcandies, vios):
#     #First cut: Pick one at random!
#     # return random.choice(vios)
#     #Second cut: Always the first!
#     return vios[0]
#
# def fix(lscores, lcandies, curr_vio,):
#     higher_score_ix, is_left = curr_vio
#     lower_score_candies = lcandies[higher_score_ix + (-1 if is_left else +1)]
#     lcandies[higher_score_ix] = 1 + lower_score_candies
#
#
# def brute_force_approach(lscores, lcandies,):
#     while True:
#         vios = find_all_violations(lscores, lcandies)
#         if len(vios) <= 0:
#             return sum(lcandies)
#         curr_vio = violation_to_fix(lscores, lcandies, vios,)
#         fix(lscores, lcandies, curr_vio,)
#     return None


def candies(n, arr):
    assert n == len(arr)
    lcandies = [1] * n
    # rv = candies_impl(arr, lcandies, [0, n])
    # rv = brute_force_approach(arr, lcandies,)
    rv = simple_attempt(arr,)
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
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)

    # fptr.write(str(result) + '\n')
    print(result)

    # fptr.close()
