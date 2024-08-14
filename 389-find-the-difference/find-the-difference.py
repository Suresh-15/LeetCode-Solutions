class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t, s = list(t), list(s)
        for i in range(len(t)):
            if t.count(t[i]) == s.count(t[i]) + 1:
                return t[i]
