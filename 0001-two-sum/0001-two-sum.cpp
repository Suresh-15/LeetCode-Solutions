class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> result;
        map<int, int> dict;

        for (int i = 0; i < nums.size(); i++) {
            int key = target - nums[i];
            if (dict.count(key) > 0) {
                result.push_back(dict[key]);
                result.push_back(i);
                break;
            } else {
                dict[nums[i]] = i;
            }
        }
        return result;
    }
};