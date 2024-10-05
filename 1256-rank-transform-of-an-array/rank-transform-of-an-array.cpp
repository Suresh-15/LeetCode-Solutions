class Solution {
public:
    vector<int> sort_and_unique(vector<int>& arr) {
        unordered_set<int> s(arr.begin(), arr.end());
        vector<int> nums(s.begin(), s.end());
        sort(nums.begin(), nums.end());
        return nums;
    }
    vector<int> arrayRankTransform(vector<int>& arr) {
        if (arr.empty()) return arr;

        vector<int> nums = arr;
        sort(nums.begin(), nums.end());
        unordered_map<int, int> ranks;

        int rank = 1;
        ranks[nums[0]] = rank++;
        for (int i = 1; i < nums.size(); ++i) {
            if (nums[i] != nums[i - 1]) {
                ranks[nums[i]] = rank++;
            }
        }

        for (int i = 0; i < arr.size(); ++i) {
            nums[i] = ranks[arr[i]];
        }
        return nums;
    }
};