class Solution:
    def convert(self, s: str, numRows: int) -> str:
        m = [[] for _ in range(numRows)]
        index, zigzag = 0, 0
        if numRows == 1 or numRows >= len(s):
            return s

        for i in s:
            m[index].append(i)
            if index == 0:
                zigzag = 1
            elif index == numRows - 1:
                zigzag = -1
            index += zigzag

        for i in range(numRows):
            m[i] = "".join(m[i])

        return "".join(m)
