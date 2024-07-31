class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        output = ""
        first, last = strs[0], strs[-1]

        for ch1, ch2 in zip(first, last):
            if ch1 == ch2:
                output += ch1
            else:
                break

        return output


        """
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
        """

        