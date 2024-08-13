class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dictionary = {}
        for i in range(len(s)):
            if s[i] not in dictionary:
                if t[i] not in dictionary.values():
                    dictionary[s[i]] = t[i]
                else:
                    return False
            elif dictionary[s[i]] != t[i]:
                return False
        return True
