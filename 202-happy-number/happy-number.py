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
        while n != 1:
            n = sum_of_squares(n)
            if n in history:
                return False
            else:
                history.add(n)
                
        return True
