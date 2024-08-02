class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] >= target:
                index = i
                break
        else:
            index = i + 1
        return index
