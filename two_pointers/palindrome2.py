"""
Write a function that takes a string as input and checks whether it can be a
valid palindrome by removing at most one character from it.
"""

def can_be_palindrome(s):
    return palindrome(s, 1)


def palindrome(s, k):
    """
    Can s be a palindrome with at most k characters deleted?
    """
    start, end = 0, len(s) - 1
    while start < end:
        if s[start] == s[end]:
            start += 1
            end -= 1
        elif k > 0:
            return palindrome(s[start + 1:end + 1], k - 1) or palindrome(s[start:end], k - 1)
        else:
            return False
    return True
