#!/bin/python3
# 15:51


####
# NOTE: From the comments it seems this might be a flawed testcase that always times out on their
#server.


import math
import os
import random
import re
import sys




# def branch_search(new_a, new_b):
#     """The point is sometimes we get tricked by an upper-case conversion that isn't the one
#     intended. Thanks to the magic of recursion I *THINK* we can just branch into two cases here,
#     the one where we found the right match and the one where the next possible match is the right one."""
#     if char_by_char(new_a[1:], new_b[1:], True):
#         #The case where matching on the present character produces eventual success, so go ahead and do that.
#         return True
#     if char_by_char(new_a[1:], new_b, True):
#         #The case where lookahead is necessary. Matching by capitalizing the present character
#         # produces eventual failure, so instead look ahead and see if declining the match leads to a
#         # better match down the line.
#         return True
#     else:
#         return False

RECURSION_LIMIT = 45

grand_hash = {}

def char_by_char(a, b, level=0):
    if level >= RECURSION_LIMIT:
        return False
    if level % 10 == 0 or level > 35:
        print ("Recursion level: {}".format(level))
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
                    print ("From cache  {}{}={}".format(new_a, new_b, grand_hash[(new_a, new_b)]))
                    return grand_hash[(new_a, new_b)]
                if char_by_char(new_a[1:], new_b[1:], level+1):
                    # The case where matching on the present character produces eventual success, so go ahead and do that.

                    grand_hash[(new_a[1:], new_b[1:])] = True
                    grand_hash[(new_a, new_b)] = True
                    print ("Caching {}{}=True".format(new_a, new_b))
                    return True
                if char_by_char(new_a[1:], new_b, level+1):
                    # The case where lookahead is necessary. Matching by capitalizing the present character
                    # produces eventual failure, so instead look ahead and see if declining the match leads to a
                    # better match down the line.
                    print ("Caching 2")
                    grand_hash[(new_a[1:], new_b)] = True
                    grand_hash[(new_a, new_b)] = True
                    return True
                else:
                    grand_hash[(new_a, new_b)] = False
                    return False
###
        if ch.islower():
            continue    #but don't advance b
        else:
            return False
    #Have we consumed all the b? If there's any left, we fail
    return len(b) == 0

def abbreviation(a, b):
    rv = char_by_char(a, b)
    #rv = char_by_char(a[::-1], b[::-1])
    if rv:
        return('YES')
    else:
        return('NO')

def harness():
    # Here we have a substantial problem with my method. We can't just keep consuming off be
    # because the match on 'w' leaves 'erWORD' and 'ORD' so b can no longer match.
    assert 'YES' == abbreviation('WORDthenlowerWORD', 'WORDWORD')
    assert 'YES' == abbreviation('daBcd', 'ABC')
    assert 'NO' == abbreviation('AfPZN', 'APZNC')
    assert 'YES' == abbreviation('aaa', 'AAA')
    assert 'YES' == abbreviation('AbC', 'AbC')
    assert 'YES' == abbreviation('AbC', 'ABC')
    assert 'YES' == abbreviation('WthW', 'WW')
    assert 'YES' == abbreviation('WORDthenlowerWORD', 'WORDthenWORD')
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
    harness()
    exit()
    q = int(input())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        # fptr.write(result + '\n')
        print(result + '\n')

    # fptr.close()
