class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        for i in range(len(nums)):
            other = target - nums[i]
            if other in nums and nums.index(other) != i:
                return list([i, nums.index(target - nums[i])])
        """
        
        seen= {}
        for i, num in enumerate(nums):
            complement= target - num
            if complement in seen:
                return([seen[complement], i])
            elif complement not in seen:
                seen[num] = i