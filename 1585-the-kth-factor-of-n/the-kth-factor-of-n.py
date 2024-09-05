class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        count = 0
        for i in range(1, n + 1):
            if n % i == 0:
                factors.append(i)
                count += 1
            if count == k:
                return factors[-1]

        return -1
