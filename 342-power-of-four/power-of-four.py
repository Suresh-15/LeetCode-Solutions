class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # return n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555) != 0

        if n == 1:
            return True
        elif n < 1:
            return False
        elif n % 4 != 0:
            return False
        elif n == 4:
            return True
        else:
            return self.isPowerOfFour(n/4)