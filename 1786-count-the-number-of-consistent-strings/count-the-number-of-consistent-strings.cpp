class Solution {
public:
    int countConsistentStrings(string allowed, vector<string>& words) {
        vector<int> is_allowed(26);
        for (auto c : allowed) {
            is_allowed[c - 'a'] = 1;
        }
        int result = 0;
        for (auto x : words) {
            bool flag = true;
            for (auto c : x) {
                if (!is_allowed[c - 'a']) {
                    flag = false;
                    break;
                }
            }
            if (flag)
                result++;
        }
        return result;
    }
};