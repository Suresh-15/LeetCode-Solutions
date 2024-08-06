class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = 0, 0
        try:
            start = nums.index(target)
        except:
            return [-1, -1]

        if nums == []:
            return [-1, -1]
        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]

        if start == len(nums) - 1:
            return [start, start]

        end = start
        while nums[end] == nums[end + 1]:
            end = end + 1
            if end == len(nums) - 1:
                break

        return [start, end]


