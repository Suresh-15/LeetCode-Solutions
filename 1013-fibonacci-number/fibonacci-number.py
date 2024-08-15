class Solution:
    from functools import lru_cache

    @lru_cache
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        elif n > 1:
            return self.fib(n - 1) + self.fib(n - 2)
