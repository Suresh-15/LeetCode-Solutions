class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total = sum(chalk)
        quotient = k // total
        k -= total * quotient
        for i in range(len(chalk)):
            if k < chalk[i]:
                return i
            else:
                k -= chalk[i]
