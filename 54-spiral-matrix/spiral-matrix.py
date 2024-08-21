class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        row, col, d = 0, -1, 1
        result = []

        while m > 0 and n > 0:
            for _ in range(n):
                col += d
                result.append(matrix[row][col])
            m -= 1

            for _ in range(m):
                row += d
                result.append(matrix[row][col])
            n -= 1

            d *= -1

        return result

