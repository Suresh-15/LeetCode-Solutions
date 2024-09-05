class Solution {
public:
    int partitionString(string s) {
        int n = s.length();
        int i = 0;
        int count = 1;
        unordered_map<char, int> mp;
        while (i < n) {
            if (mp.size() == 0) 
                mp[s[i]] = 1;
            else if (mp.find(s[i]) == mp.end()) 
                mp[s[i]] = 1;
            else {
                count++;
                mp.clear();
                mp[s[i]] = 1;
            }
            i++;
        }
        return count;
    }
};