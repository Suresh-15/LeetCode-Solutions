class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        maxArea = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                area = min(height[i], height[j]) * (j - i)
                if area > maxArea:
                    maxArea = area
        return maxArea
        """

        maxArea = 0
        left, right, maxi = 0, len(height) - 1, max(height)


        while left < right:
            area = min(height[left], height[right]) * (right - left)
            maxArea = max(maxArea, area)
            if maxi * (right - left) <= maxArea:
                break

            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1
        return maxArea
