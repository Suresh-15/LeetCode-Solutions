class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        int n = nums.size();
        vector<int> numbers;
        vector<bool> present(n + 1, false);

        for (int i = 0; i < n; i++) {
            present[nums[i]] = true;
        } 

        for (int i = 1; i <= n; i++) {
            if (!present[i]) {
                numbers.push_back(i);
            }
        }
        return numbers;
    }
};