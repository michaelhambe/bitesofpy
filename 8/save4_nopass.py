"""
Write a function that rotates characters in a string,
in both directions:

if n is positive move characters from beginning to end, 
e.g.: rotate('hello', 2) would return llohe
if n is negative move characters to the start of the 
string, e.g.: rotate('hello', -2) would return lohel
See tests for more info. Have fun!
"""

def rotate(string, n):
    """Rotate characters in a string.
       Expects string and n (int) for number of characters to move.
    """
    if n > 0:
        shifted = string[n:] + string[:n]
    else:
        shifted = string[n:] + string[:len(string)-n]

    return shifted