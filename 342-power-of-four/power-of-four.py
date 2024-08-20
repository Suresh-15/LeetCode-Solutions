class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # return n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555) != 0

        while n != 1:
            lse = n & (-n)
            if lse == 0 or lse % 4 != 0:
                return False
            if n == lse:
                n = n // 4
            else:
                n = n // lse
        return True