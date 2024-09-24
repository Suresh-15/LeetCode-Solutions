class Solution:
    def longestCommonPrefix(self, arr1, arr2):
        prefix = {}

        for val in arr1:
            num = val
            while num > 0:
                if num not in prefix:
                    prefix[num] = 0
                prefix[num] += 1
                num //= 10

        mx = float('-inf')

        for val in arr2:
            num = val
            length = len(str(num))

            while num > 0:
                if num in prefix:
                    break
                num //= 10
                length -= 1

            mx = max(mx, length)

        return mx