class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        length = len(nums)
        k = k % length
        nums[:] = nums[-k:] + nums[:-k]
        
        