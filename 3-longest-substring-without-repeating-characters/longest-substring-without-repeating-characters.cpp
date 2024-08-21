class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int length = s.length();
        int maxLength = 0, left = 0;
        unordered_set<char> charset;

        for (int right = 0; right < length; right++) {
            if (charset.count(s[right]) == 0) {
                charset.insert(s[right]);
                maxLength = max(maxLength, right - left + 1);
            } else {
                while (charset.count(s[right])) {
                    charset.erase(s[left]);
                    left++;
                }
                charset.insert(s[right]);
            }
        }
        return maxLength;
    }
};