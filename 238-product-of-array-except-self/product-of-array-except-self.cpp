class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> res;
        int R = 1;
        res.push_back(1);
        for (int i = 1; i < nums.size(); i++) {
            res.push_back(res.back() * nums[i-1]);
        }
        for (int i = nums.size() - 1; i >= 0; i--) {
            res[i] *= R;
            R *= nums[i];
        }
        return res;
    }
};