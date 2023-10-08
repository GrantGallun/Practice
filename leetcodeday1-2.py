def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in nums:
        if target - i in nums:
            if target - i == i and nums.count(i) < 2:
                continue
            else:
                sum1 = nums.index(i)
                nums[sum1] = None
                return sorted([sum1, nums.index(target - i)])


print(twoSum("hi", [3, 2, 4], 6))
