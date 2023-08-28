def three_sum(nums, target):
    """
    Given an array of numbers `nums` and a target number `target`, return true
    if there are three elements in the array `nums` whose sum equals `target`.
    Return false otherwise.
    """
    nums = sorted(nums)
    for i, x in enumerate(nums):
        left, right = i + 1, len(nums) - 1
        while left < right:
            sum3 = x + nums[left] + nums[right]
            if sum3 < target:
                left += 1
            elif sum3 > target:
                right -= 1
            else:
                return True
    return False

