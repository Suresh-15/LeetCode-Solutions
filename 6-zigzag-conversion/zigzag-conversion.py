class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """

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

        """

        if numRows < 2:
            return s
        arr = ["" for i in range(numRows)]
        direction = "down"
        row = 0
        for i in s:
            arr[row] += i
            if row == numRows - 1:
                direction = "up"
            elif row == 0:
                direction = "down"
            if direction == "down":
                row += 1
            else:
                row -= 1
        return "".join(arr)
