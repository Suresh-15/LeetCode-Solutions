class Solution:
    def romanToInt(self, s: str) -> int:
        V = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result, i, n = 0, 0, len(s)

        while i < n:
            if i < n - 1 and V[s[i]] < V[s[i + 1]]:
                result += V[s[i + 1]] - V[s[i]]
                i += 2
            else:
                result += V[s[i]]
                i += 1
        else:
            return result
