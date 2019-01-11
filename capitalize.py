#!/bin/python3

#####################
# NOTE: I've solved this except for test cases involving multiple spaces.

# Hello      world

import math
import os
import random
import re
import sys

def cap_unless_empty(w):
    if len(w) == 0:
        return ''
    if len(w) == 1:
        return w[0].upper()
    return w[0].upper() + w[1:]

# Complete the solve function below.
def solve(s):
    try:
      print(os.environ['OUTPUT_PATH'])
    except:
      #this key does not exist on my local Ubuntu
      pass
    words = s.split(sep=' ')
    new_words = [cap_unless_empty(w) for w in words]
    # new_words = [w[0].upper() + w[1:] for w in words]
    return ' '.join(new_words)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    # with open('temp', 'w') as fptr:
    #     fptr.write(result + '\n')

    print (result)