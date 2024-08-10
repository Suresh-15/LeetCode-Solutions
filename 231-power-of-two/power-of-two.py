class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # return bin(n).count("1") == 1 and n>0
        
        if n <= 0:
            return False
        while n > 1:
            if n % 2 == 0:
                n /= 2
            else:
                return False
        return True
        