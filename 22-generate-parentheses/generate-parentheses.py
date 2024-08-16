class Solution(object):
    def generateParenthesis(self, n):
        def backtrack(curr_str, open, close):
            if len(curr_str) == 2*n:
                result.append(curr_str)
                return
            if open < n:
                backtrack(curr_str + "(", open + 1, close)
            if close < open:
                backtrack(curr_str + ")", open, close + 1)
        
        result = []
        backtrack("", 0, 0)
        return result
        