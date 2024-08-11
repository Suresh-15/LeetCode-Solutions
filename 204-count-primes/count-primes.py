class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
            
        isP = [1] * (n // 2)
        for i in range(3, int(n**0.5) + 1, 2):
            if isP[i // 2]:
                isP[(i * i) // 2 :: i] = [0] * len(isP[(i * i) // 2 :: i])
        return sum(isP)
