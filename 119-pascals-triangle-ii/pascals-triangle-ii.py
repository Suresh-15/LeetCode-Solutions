class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def factorial(i):
            fact = 1
            for i in range(1, i+1):
                fact *= i
            return fact

        result = []
        numerator = factorial(rowIndex)
        for i in range(rowIndex):
            denominator = factorial(i) * factorial(rowIndex - i)
            result.append(numerator // denominator)
        result.append(1)
        return result