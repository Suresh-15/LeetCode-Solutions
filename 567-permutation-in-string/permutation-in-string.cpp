class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int length1 = s1.length();
        int length2 = s2.length();

        if (length1 > length2) {
            return false;
        }

        vector<int> s1_chars(26, 0);
        vector<int> s2_chars(26, 0);

        for (int i = 0; i < length1; i++) {
            s1_chars[s1[i] - 'a'] += 1;
            s2_chars[s2[i] - 'a'] += 1;
        }

        if (s1_chars == s2_chars) {
            return true;
        }

        for (int i = length1; i < length2; i++) {
            s2_chars[s2[i] - 'a'] += 1;
            s2_chars[s2[i - length1] - 'a'] -= 1;
            if (s1_chars == s2_chars) {
                return true;
            }
        }
        return false;
    }
};

/*      
        if s1_chars == s2_chars:
            return True
        
        for i in range(length1, length2):
            s2_chars[ord(s2[i]) - 97] += 1
            s2_chars[ord(s2[i - length1]) - 97] -= 1
            if s1_chars == s2_chars:
                return True
        else:
            return False
*/