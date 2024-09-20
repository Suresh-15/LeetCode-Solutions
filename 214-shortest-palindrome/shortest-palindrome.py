class Solution:
    def shortestPalindrome(self, s: str) -> str:
        index = 0
        length = len(s)
        for j in range(length):
            if s[index] == s[length - j - 1]:
                index += 1
        if index == length:
            return s
        p = s[index:length][::-1]

        return p + self.shortestPalindrome(s[:index]) + s[index:]
