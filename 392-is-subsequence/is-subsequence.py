class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ptr = 0
        cp = []
        for c in t:
            if ptr < len(s) and c == s[ptr]:
                cp.append(c)
                ptr += 1
        
        f = ''.join(cp)
        return f == s
