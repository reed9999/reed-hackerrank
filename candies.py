#!/bin/python3

import math
import os
import random
import re
import sys


##
# Note that test case 2 should return: 42105
# test case 3 should return: 160929
# test case 14 should return:        204867

# The basic concept of simple_attempt is an implementation of
# https://www.hackerrank.com/challenges/candies/forum/comments/81516
# but I added the tie handling, especially the partitioning, as orginal work.
# All that remains is to refactor and do other cleanup.


PARTITION_COUNT = 5

def find_partitions(lscores,):
    #Inefficient to find all but return only the first ones. Still better than crazy recursion.
    return [i for i in range(1, len(lscores)) if lscores[i] == lscores[i-1]][:PARTITION_COUNT]


# This has grown grotesque and needs to be refactored but I'm striking while the iron is hot in
# stream of consciousness.

def simple_attempt(lscores, possible_ties=True):
    total_score = 0
    if possible_ties:
        # First find the next N ties.
        partitions = find_partitions(lscores)
        partition_count = len(partitions)
        if partition_count == 0:
            return simple_attempt(lscores, False)
        last = 0
        for i in range(partition_count-1):
            # kick off recursion for the first N-1 which should be clean now.
            index = partitions[i] #The rightmost of the two tied students
            total_score += simple_attempt(lscores[last:index], False)
            last = index
        index = partitions[partition_count-1]
        total_score += simple_attempt(lscores[last:index], True)

    n = len(lscores)
    lcandies = [1] * n      #moved here the calling code.
    for i in range(1, n):
        if lscores[i] > lscores [i-1]:
            lcandies[i] = lcandies[i-1] + 1

            # No longer need to deal with ties here.
        # if lscores[i] == lscores[i - 1]:
        #     # ties are interesting. Since it doesn't matter how the two compare,
        #     # we can split the whole thing into a new right-hand piece and recurse.
        #     n = i
        #     right_partial_answer = simple_attempt(lscores[i:])
        #     lscores = lscores[:n]
        #     lcandies = lcandies[:n]
        #     break

    for i in range(n-2, -1, -1):
        if lscores[i] > lscores [i+1] and lcandies[i] <= lcandies[i+1]:
            # This time it's important not to change it if it's already correct.
            lcandies[i] = lcandies[i+1] + 1
    return sum(lcandies)

def candies(n, arr):
    assert n == len(arr)
    lcandies = [1] * n
    # rv = candies_impl(arr, lcandies, [0, n])
    # rv = brute_force_approach(arr, lcandies,)
    rv = simple_attempt(arr, True)
    return rv

def harness():
    assert 4 == candies(3, [99, 99, 98]) #[1, 2, 1] is acceptable because of the tie score.
    tc1 = [2, 4, 2, 6, 1, 7, 8, 9, 2, 1]
    assert 19 == candies(10, tc1)
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
