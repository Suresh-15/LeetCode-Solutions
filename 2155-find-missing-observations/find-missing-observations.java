class Solution {
    public int[] missingRolls(int[] rolls, int mean, int n) {
        int[] result = new int[n];
        int sum = 0;
        for (int i : rolls) 
            sum += i;

        int missingSum = mean * (n + rolls.length) - sum;
        if (missingSum > 6 * n || missingSum < n) 
            return new int[] {};

        int expectedAvg = missingSum / n, remainder = missingSum % n;

        for (int i = 0; i < remainder; i++) 
            result[i] = expectedAvg + 1;
        for (int i = remainder; i < n; i++) 
            result[i] = expectedAvg;
        
        return result;

    }
}