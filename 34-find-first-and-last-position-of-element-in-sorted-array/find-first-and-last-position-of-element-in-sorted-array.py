class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binarySearch(left, right, boolean):
            i = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    i = mid
                    if boolean:
                        right = mid - 1
                    else:
                        left = mid + 1
            return i

        start = binarySearch(0, len(nums) - 1, True)
        end = binarySearch(0, len(nums) - 1, False)
        return [start, end]
