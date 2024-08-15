class Solution:
    def fib(self, n: int) -> int:
        fibs = [0, 1]
        for i in range(n - 1):
            fibs.append((fibs[i] + fibs[i + 1]))
        return fibs[n]