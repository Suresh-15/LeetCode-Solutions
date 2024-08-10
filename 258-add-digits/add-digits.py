class Solution:
    def addDigits(self, num: int) -> int:
        def sum_of_digits(i):
            result = 0
            while i > 0:
                result += i % 10
                i //= 10
            return result

        while num // 10 != 0:
            num = sum_of_digits(num)
        return num
