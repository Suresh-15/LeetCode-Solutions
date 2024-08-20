class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # return n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555) != 0

        if n == 1:
            return True
        if n < 1:
            return False
        elif n % 4 != 0:
            return False
        else:
            count = 1
            while 4 ** count <= n:
                if 4**count == n:
                    return True
                count += 1
            return False