class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            other = target - nums[i]
            if other in nums and nums.index(other) != i:
                return list([i, nums.index(target - nums[i])])