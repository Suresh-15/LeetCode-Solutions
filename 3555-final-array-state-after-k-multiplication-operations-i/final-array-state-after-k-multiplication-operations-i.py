class Solution:
    def getFinalState(
        self, nums: List[int], k: int, multiplier: int
    ) -> List[int]:
    
        for i in range(k):
            minimum = min(nums)
            index = nums.index(minimum)
            nums[index] *= multiplier
        else:
            return nums
