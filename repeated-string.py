#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the repeatedString function below.
def quotientWithRemainder(top, bottom):
    quotient = int(top/bottom)
    remainder = top % bottom
    return (quotient, remainder)

def repeatedString(s, n):
    (quotient, remainder) = quotientWithRemainder(n, len(s))
    LETTER = 'a'
    rv = quotient * s.count(LETTER) + s[:remainder].count(LETTER)
    return rv

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)
    print (result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
