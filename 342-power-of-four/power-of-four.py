class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # return n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555) != 0

        if n <= 0:
            return False;
        return 0.5 * log2(1.0 * int(n)) == int(log2(int(n)) / 2);