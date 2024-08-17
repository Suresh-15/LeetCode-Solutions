class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int k = 0, f = 0, n = nums.size();
        for (int i = n - 1; i >= 1; i--) {
            if (nums[i] < nums[i - 1]) {
                continue;
            } else if (nums[i] > nums[i - 1]) {
                for (int j = n - 1; j >= i; j--) {
                    if (nums[j] > nums[i - 1]) {
                        swap(nums[i - 1], nums[j]);
                        break;
                    }
                }
                reverse(nums.begin() + i, nums.end());
                f = 1;
                break;
            }
        }
        if (f == 0) {
            reverse(nums.begin(), nums.end());
        }
    }
};