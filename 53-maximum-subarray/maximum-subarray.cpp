class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int result = nums[0], total = nums[0];
        for (int i = 1; i < nums.size(); ++i) {
            total = max(total, 0) + nums[i];
            result = max(result, total);
        }
        return result;
    }
};