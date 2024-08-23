class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0]
        for num in nums:
            if abs(num) == abs(closest):
                if num > closest:
                    closest = num
            if abs(num) < abs(closest):
                closest = num
        return closest