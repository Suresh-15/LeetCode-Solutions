class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dictionary = {}
        for i, num in enumerate(nums):
            if num in dictionary:
                return True
            dictionary[num] = i
        return False
        