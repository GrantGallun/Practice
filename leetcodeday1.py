def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    nums2 = sorted(nums)
    print(nums2)
    for i in range(len(nums2)):
        for j in range(len(nums2)-1, i, -1):
            if nums2[i] + nums2[j] == target:
                print(nums)
                print(nums[nums.index(nums2[i])],nums[nums.index(nums2[j])])
                sum1=nums.index(nums2[i])
                nums[sum1]=""
                print(nums)
                return sorted([sum1, nums.index(nums2[j])])
            


print(twoSum("hi", [3,2,3], 6))

