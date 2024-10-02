class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        nums = sorted(set(arr))
        ranks = {num : rank + 1 for rank, num in enumerate(nums)}
        return [ranks[num] for num in arr]