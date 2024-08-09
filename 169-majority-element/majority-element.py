class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        max_count, element = 1, nums[0]
        numsSet = set(nums)
        for i in numsSet:
            count = nums.count(i)
            if max_count < count:
                max_count = count
                element = i
        else:
            return element
