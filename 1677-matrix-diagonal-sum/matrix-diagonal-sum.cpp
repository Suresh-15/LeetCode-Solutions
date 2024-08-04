class Solution {
public:
    int diagonalSum(vector<vector<int>>& mat) {
        int n = mat.size();
        int Sum1 = 0;
        int Sum2 = 0;

        for (int i = 0; i < n; i++) {
            Sum1 += mat[i][i];
            Sum2 += mat[i][n - i - 1];
        }

        if (n % 2 != 0) {
            Sum1 -= mat[n / 2][n / 2];
        }
        
        return Sum1 + Sum2;
    }
};