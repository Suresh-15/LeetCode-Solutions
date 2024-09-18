class Solution {
public:
    int longestValidParentheses(string s) {
        vector<int> v;
        v.push_back(-1);
        int max_length = 0;

        for (int idx = 0; idx < s.length(); idx++) {
            if (s[idx] == '(') {
                v.push_back(idx);
            } else {
                v.pop_back();
                if (v.empty()) {
                    v.push_back(idx);
                } else {
                    max_length = max(max_length, idx - v.back());
                }
            }
        }

        return max_length;
    }
};