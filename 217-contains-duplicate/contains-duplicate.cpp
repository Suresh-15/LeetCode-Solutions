class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        for (int i = 1; i < nums.size(); i++) {
            int j = i;
            int ele = nums[j];
            j--;
            for (; j >= 0 && ele < nums[j]; j--) {
                nums[j + 1] = nums[j];
            }
            nums[j + 1] = ele;
            if (j >= 0 && j < nums.size() - 1 && nums[j] == nums[j + 1])
                return true;
        }
        return false;
    }
};