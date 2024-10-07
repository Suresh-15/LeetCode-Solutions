class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for char in s:
            if stack and char == 'B':
                if stack[-1] == 'A':
                    stack.pop()
                    continue  
            if stack and char == 'D':
                if stack[-1] == 'C':
                    stack.pop()
                    continue
            
            stack.append(char)
        
        return len(stack)