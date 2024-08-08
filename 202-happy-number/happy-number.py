class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_of_squares(i):
            sqs = 0
            while i > 0:
                m = i % 10
                sqs += pow(m, 2)
                i //= 10
            return sqs

        history = set()
        while n > 1 and n not in history:
            history.add(n)
            n = sum_of_squares(n)

        return n == 1
