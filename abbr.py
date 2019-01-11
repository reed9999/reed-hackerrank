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

RECURSION_LIMIT = 600
max_recursion_so_far = 0

def cache_debug(msg):
    if True:
    # if False:
        print(msg)

def recursion_debug(msg):
    if True:
    # if False:
        print(msg)

def cache(list_of_keys, value):
    for key in list_of_keys:
        grand_hash[key] = value

def branch_search(new_a, new_b, old_level=0):
    """The point is sometimes we get tricked by an upper-case conversion that isn't the one
    intended. Thanks to the magic of recursion I *THINK* we can just branch into two cases here,
    the one where we found the right match and the one where the next possible match is the right one."""
    level = old_level
    if char_by_char(new_a[1:], new_b[1:], level + 1):
        # The case where matching on the present character produces eventual success, so go ahead and do that.
        cache([
            (new_a[1:], new_b[1:]),
            (new_a, new_b),
            ],
            True)
        cache_debug("Caching {}{}=True".format(new_a, new_b))
        return True
    if char_by_char(new_a[1:], new_b, level + 1):
        # The case where lookahead is necessary. Matching by capitalizing the present character
        # produces eventual failure, so instead look ahead and see if declining the match leads to a
        # better match down the line.
        cache([
            (new_a[1:], new_b),
            (new_a, new_b),
            ],
            True)
        return True
    else:
        cache([
            (new_a[1:], new_b),
            (new_a, new_b),
            ],
            False)
        grand_hash[(new_a, new_b)] = False
        return False
    raise RuntimeError("This should not fall through.")


grand_hash = {}

def char_by_char(a, b, level=0):
    global max_recursion_so_far
    if level >= RECURSION_LIMIT:
        return False
    if level % 20 == 0 or level > max_recursion_so_far:
        recursion_debug ("Recursion level: {}".format(level))
        max_recursion_so_far = max(max_recursion_so_far, level)
    if level > 496:
        recursion_debug("Recursion error on the way:")
        recursion_debug("\t{}".format(a))
        recursion_debug("\t{}".format(b))
        recursion_debug("*****")
    if (a, b) in grand_hash.keys():
        cache_debug("[2] From cache  {}... of len {}, {}={}".format(a[:20], len(a), len(b),
                                                                grand_hash[(a, b)]))
        return grand_hash[(a, b)]
    for i in range(len(a)):
        ch = a[i]

        #One of a few things must be true:
    # next chars match exactly
    # next chars match after we capitalize a's
    # b gets a pass because a's next char is lowercase hence deleted.

    # What isn't OK?
    # If the next a char is uppercase and not matched in b

        if len(b) > 0:
            if ch == b[0]:
                b = b[1:]
                continue
            if ch.upper() == b[0]:
                # This case is very different because of the lowerWORD problem
                new_a = a[i:]
                new_b = b
                if (new_a, new_b) in grand_hash.keys():
                    cache_debug("From cache  {}... of len {}, {}={}".format(new_a[:20], len(new_a), len(new_b), grand_hash[(new_a, new_b)]))
                    return grand_hash[(new_a, new_b)]
                # if char_by_char(new_a[1:], new_b[1:], level + 1):
                #     # The case where matching on the present character produces eventual success, so go ahead and do that.
                #
                #     grand_hash[(new_a[1:], new_b[1:])] = True
                #     grand_hash[(new_a, new_b)] = True
                #     print("Caching {}{}=True".format(new_a, new_b))
                #     return True
                if branch_search(new_a, new_b, level):
                    return True


        if ch.islower():
            continue    #but don't advance b
        else:
            return False
    #Have we consumed all the b? If there's any left, we fail
    return len(b) == 0

def abbreviation(a, b):
    max_recursion_so_far = 0
    rv = char_by_char(a, b)
    #rv = char_by_char(a[::-1], b[::-1])
    if rv:
        return('YES')
    else:
        return('NO')

def harness():
    # Here we have a substantial problem with my method. We can't just keep consuming off be
    # because the match on 'w' leaves 'erWORD' and 'ORD' so b can no longer match.
    # assert 'YES' == abbreviation('WORDthenlowerWORD', 'WORDWORD')
    # assert 'YES' == abbreviation('daBcd', 'ABC')
    # assert 'NO' == abbreviation('AfPZN', 'APZNC')
    # assert 'YES' == abbreviation('aaa', 'AAA')
    # assert 'YES' == abbreviation('AbC', 'AbC')
    # assert 'YES' == abbreviation('AbC', 'ABC')
    # assert 'YES' == abbreviation('WthW', 'WW')
    # assert 'YES' == abbreviation('WORDthenlowerWORD', 'WORDthenWORD')
    assert 'NO' == abbreviation(
        "ANzaNanaanAZnnaazzzNAznnZaaZzzaZzzznaaaaZAANnaaanZnzazaAANanZaznazznzaAaNznazzanaZznzANzznzaaZzAnanNanzzAazzZZananazAznaznNznaAAaZnnanzazANAANAnnnzazaaaanzaznAaaNZnNAnnanazaZzNzazanZnazaAzanazzaNznNzzzaaanZaAnNAanzznNaNznanAnananNnaazznznnzNznnNzzanzAaNzzzZzAnnznaanzZznzNZzZzznnnaazzzanaazzazznnanANnznzAZzNZnNnanzazNaZZzzazAnNzAzAZAazanzzZzaznnZzaaazzznnaanaazaAnzzzZaaazzzzNaaNazzaaANznazAannzAaZZaznnzznnAzaaaanaaAznazZAnzzaAzaZzzZzznzazAznnaznznnaNAazZzzazNazanzaanZaZznnznzaNzannnZZNnaznzaNaAZznazAzAzNnnanznannaznAznnnnazzNnaazAanzZnaAnnaAzaanZnZNNzannanznazAnzNanaZznAAnnnNzaznAnZZnznaanzzaNzzAZzaNzNzaZanaNzNnnnAnaaZnaaznanZnzaannanzAzazazaNannaaznNnNnzaazazAzAnAzzaNaaNnanzaaZANaaZnaAzazaZZZAznAaaZnaAnnAanaAAnznNNzNnanZzzZzzNzaZaaznnznzNnaNZannNzAnnnznAazaaaanZzzananznzzZznNNzzznnznannZzznzzaZazaNnnnZzanznazzazzanzazzZannzAzazAZnnzNZannzZaNznAZanaaanAnNzzznzZaanANZananzzZaNzzaZnnzazZanzznAaaAZZaznANNzanaaanNzAnaanaAzzZnNannznaNznANzznzZanaNNaZnzaznzZaanzznnnAANzzZananzNZnaaZaANZzNAAaz",
        "ZAANAANNNAAZZZZNNAAZZAZZZNAAAANAAANNZAZAANAZNAZZNZAAZNAZZANAZNZZZNZAAZNANANZZAZZANANAZZNAZNZNAANNANZAZNNNZAZAAAANZAZNAANNNANAZAZZAZANNAZAZANAZZAZNZZZAAANANANZZNAZNANNANANNAAZZNZNNZZNNZZANZAZZZZNNZNAANZZNZZZZNNNAAZZZANAAZZAZZNNANNZNZZNNANZAZAZZAZNZZAZANZZZAZNNZAAAZZZNNAANAAZANZZZAAAZZZZAAAZZAAZNAZANNZAAZNNZZNNZAAAANAAZNAZNZZAZAZZZZNZAZZNNAZNZNNAAZZZAZAZANZAANAZNNZNZAZANNNNAZNZAAZNAZZZNNANZNANNAZNZNNNNAZZNAAZANZNANNAZAANNZANNANZNAZNZANAZNNNNZAZNNNZNAANZZAZZZAZZAANAZNNNNAANAAZNANNZAANNANZZAZAZAANNAAZNNNZAAZAZZNZZAAANANZAAAANAZAZAZNAANANNANANZNZNANZZZZZAAAZNNZNZNAANNZNNNZNAZAAAANZZANANZNZZZNZZZNNZNANNZZNZZAAZANNNZANZNAZZAZZANZAZZANNZZAZNNZANNZAZNANAAANNZZZNZAANANANZZAZZANNZAZANZZNAAAZNZANAAANZNAANAZZNANNZNAZNZZNZANAANZAZNZAANZZNNNZZANANZNAAAZAZ",
    )
    assert 'YES' == abbreviation(
        """hHhAhhcahhacaccacccahhchhcHcahaahhchhhchaachcaCchhchcaccccchhhcaahhhhcaacchccCaahhaahachhacaahhaachhhaaaCalhhchaccaAahHcchcazhachhhaaahaahhaacchAahccacahahhcHhccahaachAchahacaahcahacaahcahacaHhccccaahaahacaachcchhahhacchahhhaahcacacachhahchcaAhhcaahchHhhaacHcacahaccccaaahacCHhChchhhahhchcahaaCccccahhcaachhhacaaahcaaaccccaacaaHachaahcchaahhchhhcahahahhcaachhchacahhahahahAahaAcchahaahcaaaaahhChacahcacachacahcchHcaahchhcahaachnachhhhcachchahhhacHhCcaHhhhcaCccccaaahcahacahchahcaachcchaachahhhhhhhhcahhacacCcchahccaaaaaHhhccaAaaaCchahhccaahhacaccchhcahhcahaahhgacahcahhchcaaAccchahhhaahhccaaHcchaccacahHahChachhcaaacAhacacaacacchhchchacchchcacchachacaahachccchhhaccahcacchaccaahaaaccccccaaaaaaaHhcahcchmcHchcchaaahaccchaaachchHahcaccaaccahcacacahAhaacaacaccaccaaacahhhcacAhaCchcaacCcccachhchchcchhchahchchahchchhchcacaachahhccacachaAhaaachchhchchchhaachahaahahachhaaaccacahhcacchhhaaachaaacAahhcachchachhhcacchacaaChCahhhccahChaachhcahacchanaaacchhhccacacchcahccchAcahacaaachhacchachccaaHacaacAhahcCh""",
        """HAHHCHAACCCAHCHHAHHAHCACCHCCHHCAAHHCACCCAHHHACAAHHHHCHHCAHHAHHAAAHAACAAHAHHCAHAHACHACHCHACACHAAHHAAAHCAHHACACAACHHHCHAHCAHCHHHAHAHACCAAAHCHHCHHCCAACCCCAACHACAACAAHACHCHAHHACCHCAHHHAAACHACAACHCACACAHHCCHAHACCCACCAACHCHHHCCCCCHCCAHHCAAHHAHHHHHHHAACCCCAHCCAAAAAHHHAAAACCAHHCAHACACCHHCHAHAHHCHAACHHHHHCCHCCAHAHCHCAAACCACCCCHACCACHHACHHACACHACCAACCCCAAAAHHAHCHHHCCAHCCHACHHAHCCACACCHAHAAACACCCCAHCCAHACCCCCCHCCHHCHHHHCHCHCAHHHACHAHAACCCAAAACHAACAAAHHAAHAAAHACHHCACHCCHCHAACHACACHHCCCCCAHCACHAAAHCHCAHACAAC""",
    )
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # harness()
    # exit()
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
