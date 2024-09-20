class Solution {
public:
    vector<vector<int>> result;
    void backtrack(int start, vector<int> &nums) {
        if (start == nums.size()) {
            result.push_back(nums);
            return;
        }
        for (int i = start; i < nums.size(); i++) {
            int temp = nums[i];
            nums[i] = nums[start];
            nums[start] = temp;

            backtrack(start + 1, nums);

            temp = nums[i];
            nums[i] = nums[start];
            nums[start] = temp;
        }
    }
    vector<vector<int>> permute(vector<int>& nums) {
        backtrack(0, nums);
        return result;
    }
};