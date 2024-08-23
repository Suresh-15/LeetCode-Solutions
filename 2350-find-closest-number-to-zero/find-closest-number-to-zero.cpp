class Solution {
public:
    int findClosestNumber(vector<int>& nums) {
        int ans = nums[0];
        
        for (int num : nums) {
            if (abs(num) <= abs(ans)) {
                if (abs(num) == abs(ans))
                    ans = (num > ans) ? num : ans;
                else
                    ans = num;
            }
        }
        return ans;
    }
};