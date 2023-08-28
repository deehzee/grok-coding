def is_palindrome(s):
    """
    Given a string `s`, return true if `s` is a palindrome, return false
    otherwise.
    """
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
