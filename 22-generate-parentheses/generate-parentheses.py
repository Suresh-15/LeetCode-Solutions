class Solution(object):
    def generateParenthesis(self, n):
        generated_parenthesis = []
        def backtrack(num_open, num_closed, parens):
            if num_open == n and num_closed == n:
                generated_parenthesis.append(parens)
                return
            if num_open < num_closed:
                return
            if num_open < n:
                backtrack(num_open + 1, num_closed, parens + '(')
            if num_closed < num_open:
                backtrack(num_open, num_closed + 1, parens + ')')

        backtrack(0, 0, '')
        return generated_parenthesis
        