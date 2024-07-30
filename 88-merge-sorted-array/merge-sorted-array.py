class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
       
        first, second, ind = m-1, n-1, m + n - 1

        while second >= 0:
            if  first >= 0 and nums1[first] > nums2[second]:
                nums1[ind] = nums1[first]
                first -= 1
            else:
                nums1[ind] = nums2[second]
                second -= 1
            ind -= 1