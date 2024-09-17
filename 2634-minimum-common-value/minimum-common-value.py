class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = set(nums1), set(nums2)
        result = n1.intersection(n2)
        if result:
            return min(result)
        return -1
