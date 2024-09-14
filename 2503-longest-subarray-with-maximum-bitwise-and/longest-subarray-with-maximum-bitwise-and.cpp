class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int max_num = nums[0];
        for (int i = 0; i < nums.size(); i++)
            if (nums[i] > max_num)
                max_num = nums[i];

        int temp_len = 0, max_len = 0;
        for (int n = 0; n < nums.size(); n++) {
            if (nums[n] != max_num) {
                if (temp_len > max_len)
                    max_len = temp_len;
                temp_len = 0;
            } else
                temp_len += 1;
        }

        if (temp_len > max_len)
            return temp_len;
        return max_len;
    }
};