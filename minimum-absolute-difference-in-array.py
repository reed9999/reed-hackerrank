#!/bin/python3

import math
import os
import random
import re
import sys

def minimumAbsoluteDifference(arr)
    arr.sort!
    # Code adapted from https://stackoverflow.com/questions/310426/list-comprehension-in-ruby
    # but I don't know if [i] and [i-1] really make sense with map. It's practice for me in 
    # adapting list comprehensions though.
    return ((1..arr.length-1).map{|i| (arr[i] - arr[i-1]).abs}).min
end

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
