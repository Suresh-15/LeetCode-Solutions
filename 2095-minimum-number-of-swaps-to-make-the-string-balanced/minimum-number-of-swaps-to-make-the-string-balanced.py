class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        unbalanced = 0
        for bracket in s:
            if bracket == "[":
                stack.append(bracket)
            else:
                if not stack:
                    unbalanced += 1
                else:
                    stack.pop()

        return (unbalanced + 1) // 2
