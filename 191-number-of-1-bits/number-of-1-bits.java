class Solution {
    public int hammingWeight(int n) {
        int ones = 0;
        while(n > 0){
            int bit = n & 1;
            ones += bit;
            n = n >> 1;
        }
        return ones;
    }
}