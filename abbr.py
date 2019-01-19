#!/bin/python3
####
# NOTE: From the comments it seems this might be a flawed testcase that always times out on their
# server.
# See https://www.hackerrank.com/challenges/abbr/forum/comments/529377
# https://www.hackerrank.com/challenges/abbr/forum/comments/318643

import math
import os
import random
import re
import sys

RECURSION_LIMIT = 498
max_recursion_so_far = 0
COUNTER = 0
grand_hash = {}


def cache_debug(msg):
    print(msg)
    # pass

def recursion_debug(msg):
    print(msg)
    # pass

def cache(key, value):
    #Oops.... I was iterating through a bunch of keys, but now it should just take one single key,
    # which is a tuple.
    assert len(key) == 2
    cache_debug("Cache storing: {} -- {}".format(key, value))
    grand_hash[key] = value


# Last attempt was a complete mess. Let's try something less error-prone.
def fancier_branch_search(a, b, level=0):
    if len(a) < len(b):
        return False
    b_char = b[0]
    assert b_char.isupper()
    current_a = a
    all_occurrences = [match.start() for match in re.finditer(b[0], current_a, re.IGNORECASE)]
    recursion_debug("All occurrences:{}".format(all_occurrences))

def find_valid_occurrences(a, ch):
    """We get to this point when, for example, werWORD matches w.
    Parameters
    ----------
    a : string
        right side of our original a, starting at the lower case character that might match the
        character under consideration in b.
    ch : character
        the current character from b under consideration, i.e. the first char of the remainder of
        original b, which is being 'consumed' in a loop by the calling script.
    """
    possible_matches = []
    for i in range(len(a)):
        if a[i].isupper():
            # That's it. We no longer have the option of dropping letters because we can only drop
            # lowercase. So we can return now, adding on the last one if appropriate.
            if a[i].upper() == ch:
                possible_matches.append(i)
            return possible_matches
        # We are still in a series of lowercase letters at the start of a. For all we know, these
        # could all be dropped.
        if a[i] == ch.lower():
            possible_matches.append((i))
    recursion_debug("Possible matches are {}".format(possible_matches))
    return possible_matches

def fancy_branch_search(a, b, level=0):
    """We get to this point when, for example, werWORD matches w.
    Parameters
    ----------
    a : string
        right side of our original a, starting at the lower case character that might match the present or
        the future b (itself a remainder).
    b : string
        the remainder of original b, which is being 'consumed' in a loop by the calling script.
    """
    if len(a) < len(b):
        return False
    b_char = b[0]
    occurrences = find_valid_occurrences(a, b_char)
    #This will be buggy. I need to replace truncated_a
    truncated_a = a

    # while True: #len(truncated_a) > 0: #We may no longer need a while loop bc of for loop below.

    # Let's look for the next character of a in what remains of b to help avoid so much recursion
    # However this implementation is proving to be extremely error
    # last_index = truncated_a.lower().rfind(b_char.lower())
    if len(occurrences) == 0:
        cache((truncated_a, b), False)
        return False
    # Try all the matches starting with the rightmost/shortest(?) to see if any of them can pass the test.
    for i in range (len(occurrences)-1, -1, -1):
        index_of_char_match = occurrences[i]
        if i == 0:
            #I really don't know how to handle this yet. Need to think more.
            # But this is sort of a degenerate case. allowing the call to abbreviation_impl at
        # i=0 means
        # infinite recursion.
            raise NotImplementedError

        right_side_of_a = a[index_of_char_match:]
        result = abbreviation_impl(right_side_of_a, b, level + 1)
        cache((right_side_of_a, b), result)
        if result:
            return True
        # former degenerate case
        # assert b_char.isupper()
        # result = abbreviation_impl(a[1:], b[1:], level + 1)
        # cache((a[1:], b[1:]), result)
        # return result
        # if abbreviation_impl(truncated_a[last_index:], b, level + 1):
        #
        #     return True
        # end of the former while loop

    cache((a, b), False)
    return False



def manage_recursion(a, b, level):
    global max_recursion_so_far, COUNTER

    if (COUNTER % 1000 == 999):
        print("**********    iteration {}".format(COUNTER))
        print("""a (len {}): {}
        b (len {}): {}
        level: {}""".format(len(a), a, len(b), b, level))
        print("hash size: {}".format(len(grand_hash)))
    COUNTER += 1
    if level >= RECURSION_LIMIT:
        raise RecursionError  # False was just a guess, but guessing is probably not OK.
    if level % 25 == 20 or level > 325:
        recursion_debug("Recursion level: {} (length of hash {})".format(level, len(grand_hash)))
        max_recursion_so_far = max(max_recursion_so_far, level)
    if level > 496:
        print("Recursion error on the way")
        recursion_debug("\t{}".format(a))
        recursion_debug("\t{}".format(b))
        recursion_debug("*****")
        # raise RecursionError  #Why was I raising it manually? I think to prevent a segfault.


def abbreviation_impl(a, b, level=0):
    manage_recursion(a, b, level)
    if len(a) < len(b):
        return False
    if (a, b) in grand_hash.keys():
        cache_debug("Retrieving from cache {}... of len {}, {}={}".format(a[:20], len(a), len(b),
                                                                grand_hash[(a, b)]))
        return grand_hash[(a, b)]
    for i in range(1, len(a)):
        ch = a[i]

        #One of a few things must be true:
    # next chars match exactly
    # next chars match after we capitalize a's
    # b gets a pass because a's next char is lowercase hence deleted.

    # What isn't OK?
    # If the next a char is uppercase and not matched in b

        if len(b) > 0:
            if ch == b[0]:
                b = b[1:]   #pop one character off, advance the pointer in a, and let's do it again.
                continue
            elif ch.upper() == b[0]:
                # We have a possible match in b, but this case is very different because of the
                # lowerWORD problem
                new_a = a[i:]
                if (new_a, b) in grand_hash.keys():
                    cache_debug("Retrieving (1) from cache  {}... of len {}, {}={}".format(new_a[:20], len(new_a), len(new_b), grand_hash[(new_a, new_b)]))
                    return grand_hash[(new_a, b)]
                try:
                    # if branch_search(new_a, new_b, level):
                    fancier_branch_search(new_a, b, level)
                    result = fancy_branch_search(new_a, b, level)
                    return result
                except NotImplementedError:
                    pass

        if ch.islower():
            continue    #but don't advance b
        else:
            return False
    #Have we consumed all the b? If there's any left, we fail
    rv = len(b) == 0
    cache((a, b), rv)
    return rv

# This is too slow and is certainly opaque
# def regex_approach(a, b,):
#     b_pattern = "[a-z]*"    #OK to drop any number of lower case letters.
#     for c in b:
#         # lower case in b must only match lower
#         # upper in b can match either
#         b_pattern += \
#             c.lower() if c.islower() \
#                 else "["+ c + c.lower() + "]"
#         b_pattern += "[a-z]*"
#     # print("Matching {} {}".format(b_pattern, a))
#     return re.match(b_pattern, a)

def abbreviation(a, b):
    max_recursion_so_far = 0
    rv = abbreviation_impl(a, b)
    # rv = regex_approach(a, b)
    # rv = abbreviation_impl(a[::-1], b[::-1])
    if rv:
        return('YES')
    else:
        return('NO')

def harness_easy_cases():
    assert 'YES' == abbreviation('WORDthenlowerWORD', 'WORDWORD')
    assert 'YES' == abbreviation('daBcd', 'ABC')
    assert 'NO' == abbreviation('AfPZN', 'APZNC')
    assert 'YES' == abbreviation('aaa', 'AAA')
    assert 'YES' == abbreviation('AbC', 'AbC')
    assert 'YES' == abbreviation('AbC', 'ABC')
    assert 'YES' == abbreviation('WthW', 'WW')
    assert 'YES' == abbreviation('WORDthenlowerWORD', 'WORDthenWORD')

def harness():
    # We can't just keep consuming off be
    # because the match on 'w' leaves 'erWORD' and 'ORD' so b can no longer match.
    harness_easy_cases()
    # exit()
    # assert 'YES' == abbreviation('aaaaaaaaaabaaaaaaaaaac', 'AaaBAAc')
    assert False == fancy_branch_search('aaaaaBaaaaaaaaaac', 'Ac')
    assert 'NO' == abbreviation('aaaaaaaaaaBaaaaaaaaaac', 'AaaaAAc')
    with open('testcases/abbr12.txt') as the_file:
        lines = the_file.readlines()
        tc12_0 = (lines[1].strip(), lines[2].strip())
        tc12_7 = (lines[15].strip(), lines[17].strip())
    assert 'NO' == abbreviation(*tc12_7)
    assert 'YES' == abbreviation(*tc12_0)
    with open('testcases/abbr13.txt') as the_file:
        lines = the_file.readlines()
        # tc13_5 = tuple(lines[11:13])
        # tc13_6 = tuple(lines[13:15])
    # assert 'NO' == abbreviation(*tc13_5)
    # assert 'YES' == abbreviation(*tc13_6)
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    harness()
    exit()
    q = int(input())

    for q_itr in range(q):
        a = input()

        b = input()
        try:
            result = abbreviation(a, b)
        except RecursionError as the_error:
            print ("Recursion Error")


        # fptr.write(result + '\n')
        print(result)

    # fptr.close()


# This is too slow and is certainly opaque
# def regex_approach(a, b,):
#     b_pattern = "[a-z]*"    #OK to drop any number of lower case letters.
#     for c in b:
#         # lower case in b must only match lower
#         # upper in b can match either
#         b_pattern += \
#             c.lower() if c.islower() \
#                 else "["+ c + c.lower() + "]"
#         b_pattern += "[a-z]*"
#     # print("Matching {} {}".format(b_pattern, a))
#     return re.match(b_pattern, a)


# Outdated but maybe worth revisiting?
# def lookahead_is_ok(new_a, new_b):
#     """Quicker heuristics to attempt to remove some of the recursion. In what cases do we know that calling abbreviation_impl
#     a second time after advancing the b pointer can't possibly succeed?
#     1. If a is shorter than b, it can never be made to match b.
#     2. If the next occurrence of the next letter comes only after upper case of another letter
#     3. Anything else?"""
#     if len(new_a) + 1 < len(new_b):
#         return False
#     current_char = new_b[0]
#     next_occurrence = new_a[1:].upper().find(current_char.upper()) + 1
#     for c in new_a[1:next_occurrence]:
#         if c.isupper():
#             return False
#     return True


## Alternative implementations


def regex_find_valid_occurrences(a, ch):
    """There are some errors in my regexes so I'm trying something different. """
    # There can be no valid index beyond the next string of lower case letters, unless the letter matches exactly
    pattern = "([a-z]*{}?)".format(ch.upper())
    recursion_debug("Regex is {}".format(pattern))
    matches = []
    match = re.search(pattern, ch)
    while match:
        matches.append(match)
        match = re.search(pattern, ch)
    recursion_debug("Matches are {}".format(matches))
    return matches

def another_broken_fancy_branch_search(a, b, level=0):
    if len(a) < len(b):
        return False
    current_char = b[0]
    truncated_a = a #We may no longer need this.
    while len(truncated_a) > 0: #We may no longer need a while loop bc of for loop below.
        # Let's look for the next character of a in what remains of b to help avoid so much recursion
        # However this implementation is proving to be extremely error
        # last_index = truncated_a.lower().rfind(current_char.lower())
        occurences = find_valid_occurrences(truncated_a, current_char)
        if len(occurences) == 0:
            cache((truncated_a, b), False)
            return False
        # Try all the matches starting with the shortest one (?) to see if they pass in toto
        for i in range (len(occurences)-1, -1, -1):
            result = abbreviation_impl(occurences[i], b, level + 1)
            cache((occurences[i], b), result)
            if result:
                return True
            # former degenerate case
            # assert current_char.isupper()
            # result = abbreviation_impl(a[1:], b[1:], level + 1)
            # cache((a[1:], b[1:]), result)
            # return result
        # if abbreviation_impl(truncated_a[last_index:], b, level + 1):
        #
        #     return True
        cache((a, b), False)
        return False

def broken_fancy_branch_search(a, b, level=0):
    if len(a) < len(b):
        return False
    current_char = b[0]
    truncated_a = a
    while len(truncated_a) > 0:
        # Let's look for the next character of a in what remains of b to help avoid so much recursion
        # However this implementation is proving to be extremely error
        last_index = truncated_a.lower().rfind(current_char.lower())
        if last_index == -1:
            cache((truncated_a, b), False)
            return False
        elif last_index == 0:
            # degenerate case
            assert current_char.isupper()
            result = abbreviation_impl(a[1:], b[1:], level + 1)
            cache((a[1:], b[1:]), result)
            return result
        if len(truncated_a[last_index:]) < len(b):
            truncated_a = truncated_a[:last_index] #DRY
            continue
        if abbreviation_impl(truncated_a[last_index:], b, level + 1):

            return True
        cache((truncated_a[last_index:], b), False)
        truncated_a = truncated_a[:last_index]
