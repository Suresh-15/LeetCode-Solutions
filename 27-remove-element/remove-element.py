class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        while val in nums:
            nums.remove(val)
        return len(nums)
        """

        l, r = 0, len(nums) - 1
        while l <= r:
            while nums[r] == val and r >= 0:
                r -= 1
            if nums[l] == val:
                temp = nums[r]
                nums[r] = nums[l]
                nums[l] = temp
            else:
                l += 1
        return l
