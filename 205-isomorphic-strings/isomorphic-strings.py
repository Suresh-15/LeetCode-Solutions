class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        replace = {}
        for i in range(len(s)):
            if s[i] not in replace.keys() and t[i] in replace.values():
                return False
            elif s[i] not in replace.keys():
                replace[s[i]] = t[i]
            elif replace[s[i]] != t[i]:
                return False
        else:
            return True
