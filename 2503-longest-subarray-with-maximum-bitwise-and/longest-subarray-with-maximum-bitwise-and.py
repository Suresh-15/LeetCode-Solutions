class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans, max_val, curr_streak = 0, 0, 0
        for num in nums:
            if max_val < num:
                max_val = num
                ans, curr_streak = 0, 0
            if max_val == num:
                curr_streak += 1
            else:
                curr_streak = 0
            ans = max(ans, curr_streak)

        return ans
