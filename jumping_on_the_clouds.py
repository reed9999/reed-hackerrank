#!/bin/python3
#Starting thinking 13:55 Mon
# Naive brute force: Find the legal routes by rejecting illegal ones.
#   Count them up and take the minimum.
# Better: If the above runs out of memory in tests, think about a trickier
#   way. Maybe recursion?

# One Pomodoro so far.

import math
import os
import random
import re
import sys

class IllegalCloudsError(RuntimeError):
    pass

### BAD IMPLEMENTATION
def new_node(c, start_pos, history, step):
    if c[start_pos + step] == 1:
        history.append(pos)
        return history
    elif c[start_pos + step] == 1:
        raise IllegalCloudsError
    assert False, "There shouldn't be any way to reach this."

def append_paths_for_pos(c, start_pos, history, legal_paths):
    try:
        legal_paths.append(new_node(c, start_pos, history, 1))
        append_paths_for_pos(c, start_pos + 1, history, legal_paths)
    except:
        pass
    try:
        legal_paths.append(new_node(c, start_pos, history, 2))
        append_paths_for_pos(c, start_pos + 2, history, legal_paths)
    except:
        pass

    
def new_implementation(c):
    pointer = len(c) - 1
    hops = 0
    print("starting pointer {}".format(pointer))
    while pointer > 0:
        if c[pointer-2]==0:
            pointer -= 2
        else:
            if c[pointer-1]!=0:
                print( "There is no way to get to {}".format(pointer))
                return None
            pointer -= 1
        hops += 1
        print("new pointer {} hops {}".format(pointer, hops))
        continue
    return hops

def all_legal_paths(c):
    pass
    
def jumpingOnClouds(c):
    return new_implementation(c)

def harness():
    assert jumpingOnClouds([0]) == 0, 'i'
    assert jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]) == 4, 'sample input 0'
    assert jumpingOnClouds([1]) == None, 'ii'

if __name__ == '__main__':
    harness()

#if __name__ == '__main__':
if False:

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    print(str(result) + '\n')
