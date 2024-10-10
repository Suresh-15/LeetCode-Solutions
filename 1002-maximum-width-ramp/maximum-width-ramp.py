class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n, max_width, indices_stack = len(nums), 0, []
        for index in range(n):
            if not(indices_stack) or nums[index] < nums[indices_stack[-1]]:
                indices_stack.append(index)
            
        for index in range(n - 1, -1, -1):
            while indices_stack and nums[indices_stack[-1]] <= nums[index]:
                max_width = max(max_width, index - indices_stack[-1])
                indices_stack.pop()

        return max_width        