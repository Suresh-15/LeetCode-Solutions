class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        def find_factors(num):
            factors = []
            for i in range(1, num + 1):
                if num % i == 0:
                    factors.append(i)
            return factors

        factors = find_factors(n)
        return factors[k - 1] if k <= len(factors) else -1