class Solution {
public:
    int partitionString(string s) {
        std::array<bool, 26> att = {};
        int count = 0;
        for (auto ch : s) {
            if (att[ch - 'a'] > 0) {
                att.fill(false);
                ++count;
            }
            att[ch - 'a'] = true;
        }
        ++count; 
        return count;
    }
};