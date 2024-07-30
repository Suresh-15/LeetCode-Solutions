import math

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            q = abs(dividend) // abs(divisor)
        else: 
            q = -1 * (abs(dividend) // abs(divisor))

        if q < -1 * 2**31:
            return -1 * 2**31
        elif q > 2**31 - 1:
            return 2**31 - 1
        else:
            return q
