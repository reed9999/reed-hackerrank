import re
import the_minion_game_data as data
TC3 = """BANANANAAAS"""
# See discussion below

HUNDRED = data.TC5[:100]
TWOK = data.TC5[:2000]
THREEK = data.TC5[:3000]
FOURK = data.TC5[:4000]
DODGY = data.TC5[:4250]
# ABBREV5 = data.TC5[:5000] between 4k and 5k causes problems.
# Setting ulimit -v 2000000 is too small for 4k, ok for 1000.
    


def winning_name(vowel_score, consonant_score):
    VOWEL_PLAYER = "Kevin"
    CONSONANT_PLAYER = "Stuart"
    DRAW = "Draw"
    if vowel_score > consonant_score:
        return VOWEL_PLAYER
    if consonant_score > vowel_score:
        return CONSONANT_PLAYER
    assert vowel_score == consonant_score, "Incoherent outcome! v {} c {}".format(vowel_score, consonant_score)
    return DRAW

def scores_starting_at_position(pos, length):
    # The trick to the problem. We don't need THE SUBSTRINGS themselves, just a count of them.
    # If we know the position of a given character, we can credit 
    # all valid substrs without knowing the rest of their contents.
    return length - pos

def anomalous_draw_handling(score):
    # This function is my way of highlighting that it's illogical that a draw wouldn't print the score but that's how
    # the problem is specified.
    print (score)
    
def minion_game(s):
    all_vowels = 'AEIOU'
    # total count is just math -- 'triangular' number summing n, n-1, n-2,... 1.
    n = len(s)
    total_substrings = int(n * (n+1) / 2)
    # print("Tot {}".format(total_substrings))
    list_of_vowel_scores = [
        scores_starting_at_position(x, n) for x in range(0, n)
        if s[x].upper() in all_vowels]
    vowel_score = sum(list_of_vowel_scores)
    consonant_score = total_substrings - vowel_score
    the_tuple = (name, winning_score) = (winning_name(vowel_score=vowel_score, consonant_score=consonant_score),
                                         max(vowel_score, consonant_score))
    if vowel_score == consonant_score:
        anomalous_draw_handling(the_tuple[0])
    else:
        # print("{} {}".format(vowel_score, consonant_score))
        print("{} {}".format(the_tuple[0], the_tuple[1]))
    return the_tuple

if __name__ == '__main__':
    print ("Input?")
    # for s in ['banana', 'oiseau', '1234']:


    assert scores_starting_at_position(0, 1) == 1
    assert scores_starting_at_position(0, 2) == 2
    assert scores_starting_at_position(1, 2) == 1
    assert scores_starting_at_position(10, 50) == 40
    for (s, name, score) in [
        ('aba', 'Kevin', 4),
        (TC3, 'Draw', 33),
        (HUNDRED, 'Kevin', 2550),
        (TWOK, 'Kevin', 1001000),# should be 2000 * 2002 / 4 = 1001000
        # (THREEK, 999),
        # (FOURK, 999),
        # (DODGY, 999),
    ]:

        tup = minion_game(s)
        #print("{} {}".format(tup[0], tup[1]))
        print ("Len of string: {}".format(len(s)))
        assert tup[0] == name, "NAME WRONG {}".format(tup[0])
        assert tup[1] == score, "SCORE WRONG {}".format(tup[1])



# I misread the problem and started with the set version, but I like that too.

#
# def set_of_substr(s):
#     return {s[i:j] for i in range(0, len(s)) for j in range (i+1, len(s)+1)}
#
# def minion_game(s):
#     substrs = set_of_substr(s)
#     vowel_score = len({x for x in substrs if re.match('^[aeiou]', x, re.IGNORECASE)})
#     return vowel_score
#     return set_of_substr(s)



##### So what's going wrong?


# Kevin 25005000

# There are 5000 occurrences of A, and vowel win must start with one.
# The first (position 0) has 10k different possible substring lengths.
# The second (2) has 9998
# The last (pos 9998) has 2.

# E.g. at 4 chars, 
# ABAB ABA AB A : 4 choices
# ..AB ...A: 2 choices.


# Summing pairwise: 2 + 10000, 4 + 9998, etc. 
# 5000 numbers means 2500 pairs. Each pair sums to 10002
# 25005000
# Where did my formula go wrong? Because I misstated the number of possibles.
# (n+2), not (n+1)
