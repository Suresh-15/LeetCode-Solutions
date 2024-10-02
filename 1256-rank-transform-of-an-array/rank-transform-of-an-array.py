class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        nums = list(dict.fromkeys(arr))
        nums.sort(reverse=False)
        values = [x for x in range(1, len(nums) + 1)]
        dictionary = dict(zip(nums, values))
        ranks = []
        for num in arr:
            ranks.append(dictionary[num])
        return ranks