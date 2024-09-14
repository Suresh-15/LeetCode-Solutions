class Solution {
    public int[] xorQueries(int[] arr, int[][] queries) {
        int n = arr.length;
        int[] p = new int[n];
        p[0] = arr[0];
        for (int i = 1; i < n; i++) 
                p[i] = p[i - 1] ^ arr[i];

        int rows = queries.length;
        int[] res = new int[rows];
        for (int i = 0; i < rows; i++) {
            int l = queries[i][0];
            int h = queries[i][1];
            if (l == 0)
                res[i] = p[h];
            else
                res[i] = p[h] ^ p[l - 1];
        }
        return res;
    }
}