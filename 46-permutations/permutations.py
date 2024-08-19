class Solution(object):
    def permute(self, nums):
        def backtrack(nums):
            if not nums:
                return []
            elif len(nums)==1:
                return [nums]
            result = []
            for i,num in enumerate(nums):
                remained_perm = backtrack(nums[:i]+nums[i+1:])
                for perm in remained_perm:
                    result.append([num]+perm)
            return result
        
        return backtrack(nums)

        