class Solution {
public:
    bool canArrange(vector<int>& arr, int k) {
        vector<int> freq(k, 0);
        for (int i = 0; i < arr.size(); i++) {
            freq[((arr[i] % k) + k) % k] += 1;
        }

        if (freq[0] % 2 != 0) {
            return false;
        }
        for (int i = 1; i < (k / 2) + 1; i++) {
            if (freq[i] != freq[k - i]) {
                return false;
            }
        }
        return true;
    }
};