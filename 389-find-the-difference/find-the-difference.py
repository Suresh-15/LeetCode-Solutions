class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(reduce(operator.xor, map(ord, s + t)))
