class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        return max((n,len([*g]))for n,g in groupby(nums))[1]
