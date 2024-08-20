class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # return n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555) != 0

        if n == 0:
            return False
        if n & n - 1 == 0:
            n = bin(n)[2:]
            if len(n) % 2 != 0:
                return True
        return False
