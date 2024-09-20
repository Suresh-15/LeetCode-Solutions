class Solution {
public:
    string shortestPalindrome(string s) {
        int index = 0;
        int length = s.length();
        for (int j = 0; j < length; j++) {
            if (s[index] == s[length - j - 1]) {
                index += 1;
            }
        }

        if (index == length) {
            return s;
        }

        string p = s.substr(index, length);
        reverse(p.begin(), p.end());
        return p + shortestPalindrome(s.substr(0, index)) + s.substr(index);
    }
};