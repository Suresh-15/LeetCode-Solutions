class Solution {
public:
    void swap(char& a, char& b) {
        char t = a;
        a = b;
        b = t;
    }

    bool isVowel(char a) {
        if (a == 'a' || a == 'A' || a == 'e' || a == 'E' || a == 'i' ||
            a == 'I' || a == 'o' || a == 'O' || a == 'u' || a == 'U')
            return true;
        else
            return false;
    }

    string reverseVowels(string s) {
        int l = 0, r = s.length() - 1;
        while (l <= r) {
            bool left = isVowel(s[l]);
            bool right = isVowel(s[r]);
            if (left && right) {
                swap(s[l], s[r]);
                l++;
                r--;
            } else if (!left) {
                l++;
            } else if (!right) {
                r--;
            }
        }

        return s;
    }

    /*
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
    */
};
