class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        def function(string):
            h = {'a': 0, 'e': 0, 'i':0, 'o': 0, 'u':0}
            for i in string:
                if i in h.keys():
                    h[i] += 1
            
            print(h)
            for j in h.values():
                if j % 2 != 0:
                    return False
            else:
                return True

        k = n = len(s)
        while k > 0:
            for i in range(n - k + 1):
                if function(s[i : i + k]):
                    return k
            k -= 1

        return 0