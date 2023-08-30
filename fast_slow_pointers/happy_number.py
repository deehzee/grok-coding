"""
Write an algorithm to determine if a number is a happy number.

We use the following process to check if a given number is a happy number:

    * Starting with the given number n, replace the number with the sum of the
    squares of its digits.

    * It enters a cycle, which will depict that the given number n is not a
    happy number.

Return true if n is a happy number, false otherwise.

"""


def sum_square_digits(n):
    ss = 0
    while n > 0:
        n, d = n // 10, n % 10
        ss += d * d
    return ss


def is_happy_number(n):
    """Return whether n is a happy number."""
    slow, fast = n, sum_square_digits(n)
    while slow != 1 and fast != 1 and slow != fast:
        slow = sum_square_digits(slow)
        fast = sum_square_digits(sum_square_digits(fast))
    return fast == 1 or slow == 1

