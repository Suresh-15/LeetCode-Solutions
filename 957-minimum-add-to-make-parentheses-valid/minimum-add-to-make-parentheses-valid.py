class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        min_count = 0 
        open_deficit = 0

        for char in s: 
            if char == "(":
                open_deficit += 1
            else:
                if open_deficit == 0:
                    min_count += 1
                else:
                    open_deficit -= 1
        
        return min_count + open_deficit