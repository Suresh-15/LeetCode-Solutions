class Solution {
public:
    bool allZero(int* arr) {
        for (int i = 0; i < 26; i++) {
            if (arr[i] != 0) {
                return false;
            }
        }
        return true;
    }
    bool checkInclusion(string s1, string s2) {
        int length1 = s1.length();
        int length2 = s2.length();

        if (length1 > length2) {
            return false;
        }

        int arr[26] = {0};
        for (int i = 0; i < length1; i++) {
            arr[s1[i] - 'a'] += 1;
        }
        for (int i = 0; i < length2; i++) {
            arr[s2[i] - 'a']--;
            if (i - length1 >= 0) {
                arr[s2[i - length1] - 'a'] += 1;
            }
            if (allZero(arr)) {
                return true;
            }
        }
        return false;

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