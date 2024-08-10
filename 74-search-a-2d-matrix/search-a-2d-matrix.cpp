class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int rows = matrix.size(), cols = matrix[0].size();
        int top = 0, bottom = rows - 1;

        if (rows == 0 || cols == 0)
            return false;
        if (target < matrix[0][0] || target > matrix[rows-1][cols-1])
            return false;

        int mid_row = 0;
        while (top <= bottom) {
            mid_row = (top + bottom) / 2;
            if (matrix[mid_row][0] <= target && target <= matrix[mid_row][cols - 1])
                break;
            else if (target < matrix[mid_row][0])
                bottom = mid_row - 1;
            else
                top = mid_row + 1;
        }

        vector<int> target_row = matrix[mid_row];
        int left = 0, right = cols - 1;

        int mid_col;
        while (left <= right){
            mid_col = (left + right) / 2;
            if (target_row[mid_col] == target)
                return true;
            else if (target_row[mid_col] < target)
                left = mid_col + 1;
            else
                right = mid_col - 1; 
        }

        return false;
    }
};