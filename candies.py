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

# The basic concept of candies_impl is an implementation of
# https://www.hackerrank.com/challenges/candies/forum/comments/81516
# but I added the tie handling, especially the partitioning, as orginal work.
# All that remains is to refactor and do other cleanup.


PARTITION_COUNT = 5

def find_partitions(lscores,):
    #Inefficient to find all but return only the first ones. But better than crazy amounts of recursion.
    return [i for i in range(1, len(lscores)) if lscores[i] == lscores[i-1]][:PARTITION_COUNT]

def result_for_segment_without_ties(segment_scores, ):
    n = len(segment_scores)
    lcandies = [1] * n
    for i in range(1, n):
        if segment_scores[i] > segment_scores [i-1]:
            lcandies[i] = lcandies[i-1] + 1

    for i in range(n-2, -1, -1):
        if segment_scores[i] > segment_scores [i+1] and lcandies[i] <= lcandies[i+1]:
            # On the second pass it's important not to change it if it's already correct.
            lcandies[i] = lcandies[i+1] + 1
    return sum(lcandies)

def candies_impl(lscores, ):
    total_score = 0
    # First find the next N ties.
    partitions = find_partitions(lscores)
    partition_count = len(partitions)
    if partition_count == 0:
        return result_for_segment_without_ties(lscores,)
    last = 0
    for i in range(partition_count-0):
        # Call the calculator for the first N-1 which should be clean now.
        index = partitions[i] #The rightmost of the two tied students
        total_score += result_for_segment_without_ties(lscores[last:index],)
        last = index
    # Now handle the last one of the partition recursively
    total_score += candies_impl(lscores[last:],)
    return total_score

def candies(n, arr):
    assert n == len(arr)
    lcandies = [1] * n
    # rv = candies_impl(arr, lcandies, [0, n])
    # rv = brute_force_approach(arr, lcandies,)
    rv = candies_impl(arr,)
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
    harness()
    print("Harness OK")
    # exit()
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
