class Solution {
public:
    vector<int> missingRolls(vector<int>& rolls, int mean, int n) {
        vector<int> result;
        int sum = 0;
        for (int i : rolls) 
            sum += i;

        int missingSum = mean * (n + rolls.size()) - sum;
        if (missingSum > 6 * n || missingSum < n) 
            return result;

        int expectedAvg = missingSum / n, remainder = missingSum % n;

        for (int i = 0; i < remainder; i++) 
            result.push_back(expectedAvg + 1);
        for (int i = remainder; i < n; i++) 
            result.push_back(expectedAvg);
        
        return result;
    }
};