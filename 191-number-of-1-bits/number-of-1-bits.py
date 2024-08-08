class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = "{0:b}".format(n)
        count = 0
        for b in binary:
            if b == '1':
                count += 1
        return count

        """
        ones = 0
        while n > 0:
            if n % 2 == 1:
                ones += 1
            n //= 2
        return ones
        """