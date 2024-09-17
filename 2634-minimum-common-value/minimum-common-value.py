class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        num1_ptr = num2_ptr = 0
        while(num1_ptr < len(nums1) and num2_ptr < len(nums2)):
            if (nums1[num1_ptr] < nums2[num2_ptr]):
                num1_ptr += 1
            elif (nums1[num1_ptr] > nums2[num2_ptr]):
                num2_ptr += 1
            else:
                return nums1[num1_ptr]
        return -1