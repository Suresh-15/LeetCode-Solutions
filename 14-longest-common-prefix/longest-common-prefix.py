class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix, ptr = "", 0
        lengths = [len(s) for s in strs]
        for i in range(min(lengths)):
            character = strs[0][ptr]
            for j in range(len(strs)):
                if character != strs[j][ptr]:
                    break
            else:
                prefix += character
                ptr = ptr + 1
        return prefix

        