class Solution {
public:
    int countSegments(string s) {
        int n = s.length();
        int count = 0, i = 0;
        while (i < n) {
            while (i < n && s[i] == ' ')
                i += 1;
            if (i >= s.size())
                break;
            while (i < n && s[i] != ' ') 
                i += 1;
                
            count += 1;
        }
        return count;
    }
};