class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        root = sqrt(n)
        for i in range(1, ceil(root)):
            if n % i == 0:
                k -= 1
            if k == 0:
                return i

        for i in range(floor(root), 0, -1):
            if n % (n // i) == 0:
                k -= 1
            if k == 0:
                return n // i

        return -1
