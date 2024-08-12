class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        distinct_elements = list(set(nums))
        if len(distinct_elements) <= 2:
            return max(distinct_elements)
        first = second = third = float("-inf")

        for num in distinct_elements:
            if num > first:
                third = second
                second = first
                first = num
            elif num > second:
                third = second
                second = num
            elif num > third:
                third = num

        return third

        """
        distinct_elements = set(nums)
        if len(distinct_elements) <= 2:
            return max(nums)
        max1, max2, max3 = max(nums), float('-inf'), float('-inf')
        for i in nums:
            if max2 < i and i < max1:
                max2 = i
        for i in nums:
            if max3 < i and i < max2:
                max3 = i
        return max3
        """
