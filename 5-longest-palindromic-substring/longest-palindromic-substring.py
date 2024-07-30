class Solution:
    def isPalindrome(self, s: str) -> str:
        return s == s[::-1]

    def longestPalindrome(self, s: str) -> str:
        """
        for k in range(len(s), 0, -1):
            for i in range(0, len(s)-k+1):
                if self.isPalindrome(s[i: i+k]):
                    return s[i: i+k]
        """
        if s == s[::-1]:
            return s
        t, n = 0, 1
        for i in range(1, len(s)):
            l, r = i - n, i + 1
            s1 = s[l-1 : r]
            if l >= 1 and s1 == s1[::-1]:
                n += 2
                t = l - 1
            else:
                s2 = s[l:r]
                if s2 == s2[::-1]:
                    n += 1
                    t = l
        return s[t:t+n]