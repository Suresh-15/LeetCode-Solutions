class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        output = []
        self.backtrack(n, 0, 0, output, result)
        return result

    def backtrack(self, n, leftCount, rightCount, output, result):
        if leftCount >= n and rightCount >= n:
            outputStr = "".join(output)
            result.append(outputStr)

        if leftCount < n:
            output.append("(")
            self.backtrack(n, leftCount + 1, rightCount, output, result)
            output.pop()

        if rightCount < leftCount:
            output.append(")")
            self.backtrack(n, leftCount, rightCount + 1, output, result)
            output.pop()
