class Solution:
    def hammingWeight(self, n: int) -> int:
        # return bin(n).count('1')

        ones = 0
        while n > 0:
            if n % 2 == 1:
                ones += 1
            n //= 2
        return ones
        