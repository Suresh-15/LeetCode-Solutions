class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for i in range(numRows - 1):
            temp = [0] + res[i] + [0]
            newrow = []
            for i in range(1, len(temp)):
                newrow.append(temp[i - 1] + temp[i])
            res.append(newrow)
        return res
        
        """
        def factorial(i):
            fact = 1
            for i in range(1, i+1):
                fact *= i
            return fact

        def getRow(n):
            row = []
            numerator = factorial(n)
            for i in range(n):
                denominator = factorial(i) * factorial(n - i)
                row.append(numerator // denominator)
            row.append(1)
            return row

        result = [[1]]
        if numRows == 1:
            return result
        for i in range(1, numRows):
            result.append(getRow(i))
        return result
        """