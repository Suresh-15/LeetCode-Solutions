class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        """
        res = [[1]]
        for i in range (rowIndex):
            template = [0] + res[-1] + [0]
            row = []
            for j in range (len(res[-1]) + 1):
                row.append(template[j] + template[j+1])
            res.append(row)
        return res[-1]
        """

        def factorial(i):
            fact = 1
            for i in range(1, i + 1):
                fact *= i
            return fact

        result = []
        numerator = factorial(rowIndex)
        for i in range(rowIndex):
            denominator = factorial(i) * factorial(rowIndex - i)
            result.append(numerator // denominator)
        result.append(1)
        
        return result
