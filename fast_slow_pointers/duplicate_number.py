"""
Given an unsorted array of positive numbers, `nums`, such that the values lie
in the rage [1, n], inclusive, and that there are n + 1 numbers in the array,
find and return the duplicate number in the array `nums`. There is only one
repeated number in `nums`.

"""


# time: O(n log n)
def find_duplicate_naive(nums):
    nums = sorted(nums)
    n = 1
    cur, nxt = nums[0], nums[1]
    while cur != nxt:
        n += 1
        cur, nxt = nxt, nums[n]
    return cur


# time: O(n):
# Move slow pointer 1 step, and fast pointer 2 steps at a time, until they meet.
# When they intersect, move the slow pinter back to 0.
# Move both fast and slow pointer 1 step at a time, until they meet.
# This point is the entry point for the loop, and is the duplicate number,
# as this is pointed by two different numbers in the array.
def find_duplicate(nums):
    slow = fast = 0
    while True:
        slow, fast = nums[slow], nums[nums[fast]]
        if slow == fast:
            break
    slow = 0
    while slow != fast:
        slow, fast = nums[slow], nums[fast]
    return slow

