class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        if not matrix or not matrix[0]:
            return False
            
        row, col = 0, 0
        for i in range(rows):
            if matrix[i][0] <= target and matrix[i][cols-1] >= target:
                row = i
                break
        for i in range(cols):
            if matrix[row][i] == target:
                return True
        return False
