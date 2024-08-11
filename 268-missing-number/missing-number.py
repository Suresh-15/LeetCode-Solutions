class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        totalSum = n * (n + 1) // 2
        arraySum = sum(nums)
        return totalSum - arraySum
