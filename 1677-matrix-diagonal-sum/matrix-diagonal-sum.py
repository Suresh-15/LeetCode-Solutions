class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        diagonalSum, n = 0, len(mat)
        for i in range(n):
            diagonalSum += mat[i][i]
            diagonalSum += mat[i][n - 1 - i]
        if n % 2 == 1:
            diagonalSum -= mat[n // 2][n // 2]
        return diagonalSum