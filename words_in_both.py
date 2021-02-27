# Author: Paul Quaife
# Date: 2/23/2021
# Description: Takes two strings of parameters and returns what is in both.

def words_in_both(s1, s2):
    """Takes two strings in words, compares them, and returns what is similar."""
    words1 = s1.lower().split(" ")
    words2 = s2.lower().split(" ")
    result = []
    for x in words1:
        if (x in words2) and (x not in result):
            result.append(x)
    return result


print(words_in_both("She is a jack of all trades", "Jack was tallest of all"))
