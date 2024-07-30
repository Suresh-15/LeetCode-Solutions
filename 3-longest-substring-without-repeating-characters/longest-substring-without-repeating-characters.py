class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        maxLength = 0
        charset = set()
        left = 0

        for right in range(length):
            if s[right] not in charset:
                charset.add(s[right])
                maxLength = max(maxLength, right-left+1)
            else:
                while s[right] in charset:
                    charset.remove(s[left])
                    left += 1
                charset.add(s[right])
        return maxLength