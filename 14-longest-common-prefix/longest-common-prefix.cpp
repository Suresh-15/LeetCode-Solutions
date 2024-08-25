class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string result;
        int max_length = strs[0].size();
        for (int i = 1; i < strs.size(); i++) {
            if (max_length > strs[i].size()) {
                max_length = strs[i].size();
            }
        }
        
        int index = 0;
        bool valid = true;
        while (index < max_length) {
            for (int i = 0; i < strs.size() - 1; i++) {
                if (strs[i][index] != strs[i + 1][index]) {
                    valid = false;
                    break;
                }
            }
            if (valid) {
                result.push_back(strs[0][index]);
                index++;
            } else {
                break;
            }
        }
        return result;
    }
};