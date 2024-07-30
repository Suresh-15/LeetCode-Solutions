class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        ans=0
        for i in nums:
            ans=ans^i
        return ans

        """
        s = sorted(list(set(nums)))
        for i in s:
            if nums.count(i) == 1:
                return i
        """