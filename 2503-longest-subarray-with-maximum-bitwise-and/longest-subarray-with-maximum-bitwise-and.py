class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        m = max(nums)
        msf = 0
        res = 0
        for i in range(len(nums)):
            if nums[i] == m:
                msf += 1
            else:
                res = max(msf, res)
                msf = 0
        res = max(msf, res)
        return res
