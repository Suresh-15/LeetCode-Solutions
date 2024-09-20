class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        
        front = (s[1:])[::-1]
        for i in range(len(front)):
            temp = s
            t = front[:i + 1]
            temp = t + temp
            if temp == temp[::-1]:
                return temp        
        return temp