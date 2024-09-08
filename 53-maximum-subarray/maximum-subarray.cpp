class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int max_value = *std::max_element(nums.begin(), nums.end());
        if(nums.size() == 1 || max_value <= 0)
            return max_value;
        int right = nums.size() - 1;
        int sum = 0;
        while(right >= 0){
            sum += nums[right];
            max_value = max(sum, max_value);
            if(sum <= 0){
                sum = 0;
            }
            right--;
        }
        return max_value;
    }
};