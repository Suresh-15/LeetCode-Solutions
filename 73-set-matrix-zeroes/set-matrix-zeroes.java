class Solution {
    public void setZeroes(int[][] matrix) {
        if (matrix.length == 0 || matrix[0].length == 0)
            return ;
        int m = matrix.length, n = matrix[0].length;
        boolean zero_in_row1 = false;
        boolean zero_in_col1 = false;

        for (int i = 0; i < n; i++) {
            if (matrix[0][i] == 0) {
                zero_in_row1 = true;
                break;
            }
        }
        for (int i = 0; i < m; i++) {
            if (matrix[i][0] == 0) {
                zero_in_col1 = true;
                break;
            }
        }

        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (matrix[i][j] == 0) {
                    matrix[0][j] = 0;
                    matrix[i][0] = 0;
                }
            }
        }
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (matrix[0][j] == 0 || matrix[i][0] == 0)
                    matrix[i][j] = 0;
            }
        }

        if (zero_in_row1)
            for (int i = 0; i < n; i++)
                matrix[0][i] = 0;
        if (zero_in_col1)
            for (int i = 0; i < m; i++)
                matrix[i][0] = 0;
    }
}
