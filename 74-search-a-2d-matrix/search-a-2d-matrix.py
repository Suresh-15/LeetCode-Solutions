class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        top, bottom = 0, rows - 1

        while top <= bottom:
            mid_row = (top + bottom) // 2
            if matrix[mid_row][0] <= target <= matrix[mid_row][cols - 1]:
                break
            elif target < matrix[mid_row][0]:
                bottom = mid_row - 1
            else:
                top = mid_row + 1
        else:
            return False  
        
        row = matrix[mid_row]
        left, right = 0, cols - 1
        while left <= right:
            mid_col = (left + right) // 2
            if row[mid_col] == target:
                return True
            elif row[mid_col] < target:
                left = mid_col + 1
            else:
                right = mid_col - 1
        
        return False


        """
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
        """

        
        
        