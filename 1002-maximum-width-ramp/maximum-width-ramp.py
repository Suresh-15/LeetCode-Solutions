class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        ans = 0
        stack = []
        n = len(nums)

        for i in range(n):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)
        
        for i in range(n-1,-1,-1):
            while stack and nums[i] >= nums[stack[-1]]:
                ans = max(ans, i - stack.pop())
        
        return ans
   