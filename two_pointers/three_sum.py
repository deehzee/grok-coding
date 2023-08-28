def three_sum(nums, target):
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

