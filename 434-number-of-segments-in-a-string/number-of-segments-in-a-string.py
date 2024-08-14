class Solution:
    def countSegments(self, s: str) -> int:
        i, c, n = 0, 0, len(s)
        while i < n:
            while i < n and s[i] == " ":
                i += 1
            count = False
            while i < n and s[i] != " ":
                i += 1
                count = True
            if count:
                c += 1
            i += 1
        return c
