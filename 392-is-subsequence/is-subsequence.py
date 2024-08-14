class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ptr = 0
        for i in range(len(t)):
            if ptr == len(s):
                return True
            if s[ptr] == t[i]:
                ptr += 1
        else:
            if ptr == len(s):
                return True
            else:
                return False
