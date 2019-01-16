#!/bin/python3

import math
import os
import random
import re
import sys

#Only test case 05 fails. Expected: -953782

def luckBalance(k, contests):
    total = 0
    list_of_important_luck = []
    for contest in contests:
        if contest[1] == 0:
            total += contest[0]
        else:
            list_of_important_luck.append(contest[0])
    list_of_important_luck.sort()
    if k==0:
        #since negative indices have a special meaning in Python, we can't just take -0
        #Still the same algorithm though!
        return total - sum(list_of_important_luck)
    else:
        return total + sum(list_of_important_luck[-k:]) - sum(list_of_important_luck[:-k])

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    print(str(result) + '\n')
    # fptr.write(str(result) + '\n')

    # fptr.close()
