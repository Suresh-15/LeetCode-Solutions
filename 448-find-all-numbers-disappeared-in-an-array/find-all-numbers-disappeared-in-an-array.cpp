class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        vector<int> result;
        vector<bool> seen(size(nums) + 1, false);
        for (auto c : nums)
            seen[c] = true;
        for (int i = 1; i <= size(nums); i++)
            if (!seen[i])
                result.push_back(i);
        return result;
    }
};