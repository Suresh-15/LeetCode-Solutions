class Solution:
    def hammingWeight(self, n: int) -> int:
        # return bin(n).count('1')
        
        ones = 0
        while n > 0:
            bit = n & 1
            ones += bit
            n = n >> 1
        return ones
