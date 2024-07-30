class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        ans=0
        for i in nums:
            ans=ans^i
        return ans
        """
        """
        s = sorted(list(set(nums)))
        for i in s:
            if nums.count(i) == 1:
                return i
        """
        nums = sorted(nums)
        for i in range(0, len(nums), 2):
            if i == len(nums) - 1:
                return nums[i] 
            if nums[i] != nums[i+1]:
                return nums[i]


