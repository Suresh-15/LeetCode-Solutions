class Solution {
public:
    string reverseVowels(string s) {
        vector<char> c;
        vector<int> indices;
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == 'a' || s[i] == 'A' || s[i] == 'e' || s[i] == 'E' ||
                s[i] == 'i' || s[i] == 'I' || s[i] == 'o' || s[i] == 'O' ||
                s[i] == 'u' || s[i] == 'U') {
                c.push_back(s[i]);
                indices.push_back(i);
            }
        }

        int ptr = c.size() - 1;
        for (int i = 0; i < indices.size(); i++) {
            s[indices[i]] = c[ptr];
            ptr--;
        }
        return s;
    }
};