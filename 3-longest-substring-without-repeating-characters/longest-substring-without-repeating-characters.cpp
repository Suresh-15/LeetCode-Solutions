class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        bool visited[256] = {false};
        int left = 0, right = 0;
        int maxLength = 0;
        while (right < s.size()) {
            while (visited[s[right]] && left < right) {
                visited[s[left]] = false;
                left++;
            }
            visited[s[right]] = true;
            maxLength = max(maxLength, right - left + 1);
            right++;
        }
        return maxLength;
    }
};