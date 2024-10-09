class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opens = close = 0
        for char in s:
            if char == '(':
                opens += 1
            else:
                if opens >= 1:
                    opens -= 1
                else:
                    close += 1

        return opens + close 