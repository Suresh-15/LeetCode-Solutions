class Solution {
public:
    vector<vector<int>> construct2DArray(vector<int>& original, int m, int n) {
        vector<vector<int>> result(m);
        if (m * n != original.size())
            return {};

        int index = 0;
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                result[i].push_back(original[index++]);

        return result;
    }
};