class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        init_ind = {k for k in range(len(nums))}
        def dfs(indices,path,c):
            if c == len(nums):
                res.append(path)
            counter = 0
            for ind in indices:
                if counter > 0 and nums[ind] == nums[prev_ind]:
                    counter += 1
                    prev_ind = ind
                    continue
                new_indices = {elt for elt in indices}
                new_indices.discard(ind)
                prev_ind = ind
                counter += 1
                dfs(new_indices, path + [nums[ind]], c + 1)

        dfs(init_ind, [], 0)
        return res
