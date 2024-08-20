class Solution {
    public boolean isPowerOfFour(int n) {
        int c = 0;
        if ((n & (n - 1)) == 0 && n > 0) {
            while (n > 0) {
                n = n << 2;
            }
            return (n == 0);
        }
        return false;
    }
}