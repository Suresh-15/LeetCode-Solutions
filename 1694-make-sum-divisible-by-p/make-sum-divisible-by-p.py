class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        mod_nums = [x % p for x in nums]
        t = sum(mod_nums) % p

        if t == 0:
            return 0
        elif t in mod_nums:
            return 1
        seen = {0: -1}
        total = 0
        n = len(nums)
        best = n
        for j, x in enumerate(mod_nums):
            total = (total + x) % p
            targ = (total - t) % p
            if targ in seen:
                i = seen[targ]
                best = min(j - i, best)
            seen[total] = j
        if best == n:
            return -1 
        return best