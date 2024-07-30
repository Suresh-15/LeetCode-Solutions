class Solution:
    def compress(self, s: str) -> str:
        if s == '':
            return ''
        count, prev, result = 0, s[0], ''
        for i in range(len(s)):
            if prev == s[i]:
                count += 1
            else:
                result += str(count)
                result += s[i-1]
                prev = s[i]
                count = 1
        else:
            if count != 0:
                result += str(count)
                result += s[i]

        return result

    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        return self.compress(self.countAndSay(n-1))