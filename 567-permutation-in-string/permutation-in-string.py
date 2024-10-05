class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def charsArray(string):
            c = [0] * 26
            for s in string:
                c[ord(s) - ord('a')] += 1
            return c

        chars  = charsArray(s1)
        length = len(s1)
        for i in range(len(s2) - length + 1):
            if chars == charsArray(s2[i : i + length]):
                return True
        else:
            return False
