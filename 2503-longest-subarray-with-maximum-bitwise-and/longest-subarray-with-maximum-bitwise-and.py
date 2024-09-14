class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_num = max(nums)
        temp_len = max_len = 0

        for n in nums:
            if n != max_num:
                if temp_len > max_len:
                    max_len = temp_len
                temp_len = 0
            else:
                temp_len += 1

        if temp_len > max_len:
            max_len = temp_len
        return max_len
