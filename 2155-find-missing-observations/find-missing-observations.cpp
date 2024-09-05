class Solution {
public:
    vector<int> missingRolls(vector<int>& rolls, int mean, int n) {
        int total = 0, m = rolls.size();
        int m_sum = accumulate(rolls.begin(), rolls.end(), 0);
        long total_sum = (m + n) * mean;

        int n_sum = total_sum - m_sum;
        if (n_sum < n || n_sum > 6 * n)
            return {};

        int distribution = n_sum / n, remaining = n_sum % n;
        vector<int> ans(n, distribution);

        for (int i = 0; i < remaining; i++)
            ++ans[i];

        return ans;
    }
};