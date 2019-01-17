#!/bin/python3
# https://www.hackerrank.com/challenges/2d-array/problem

import math
import os
import random
import re
import sys

class TwoDArray(list):
    def __init__(self, arr):
        self._row_array = arr

    def __len__(self):
        return len(self._row_array)

    def __getitem__(self, ix):
        return self._row_array[ix]

    def hourglass(self, center):
        assert 2 == len(center)
        r, c = center
        assert r > 0
        assert r < len(self) - 1
        assert c > 0
        assert c < len(self[0]) - 1
        return [self[r - 1][c - 1:c + 2],
                self[r][c],
                self[r + 1][c - 1:c + 2],
                ]

    def hourglass_sum(self, center):
        hg = self.hourglass(center)
        the_map = (map(sum, hg))
        rv = list(the_map)
        # rv = sum(hg.map(sum))
        return rv


def hourglassSum(arr):
    arr2d = TwoDArray(arr)
    print([arr2d.hourglass_sum([i, j]) for i in range(1, 4) for j in range(1,4)])
    return max([arr2d.hourglass_sum([i, j]) for i in range(1, 4) for j in range(1,4)])

def harness():
    data = """1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
""".splitlines(False)
    arr = []
    for row in data:
        arr.append(list(map(int, row.rstrip().split())))
    result = hourglassSum(arr)
    print(result)

if __name__ == '__main__':
    harness(); exit();
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = open('temp', 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    print(str(result) + '\n')
    # fptr.write(str(result) + '\n')

    fptr.close()
