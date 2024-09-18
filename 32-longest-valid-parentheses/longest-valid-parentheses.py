class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_length = 0
        
        for idx, char in enumerate(s):
            if char == '(':
                stack.append(idx)
            else:
                stack.pop()
                if stack:
                    max_length = max(max_length, idx - stack[-1])
                else:
                    stack.append(idx)

        return max_length
