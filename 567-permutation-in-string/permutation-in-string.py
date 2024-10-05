class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length1 = len(s1)
        length2 = len(s2)

        s1_chars = [0] * 26
        s2_chars = [0] * 26

        if length1 > length2:
            return False
        for i in range(length1):
            s1_chars[ord(s1[i]) - 97] += 1
            s2_chars[ord(s2[i]) - 97] += 1
        
        if s1_chars == s2_chars:
            return True
        
        for i in range(length1, length2):
            s2_chars[ord(s2[i]) - 97] += 1
            s2_chars[ord(s2[i - length1]) - 97] -= 1
            if s1_chars == s2_chars:
                return True
        else:
            return False
