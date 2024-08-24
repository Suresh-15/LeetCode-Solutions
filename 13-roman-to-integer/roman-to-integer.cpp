class Solution {
public:
    int roman(char a) {
        if (a == 'I')
            return 1;
        else if (a == 'V')
            return 5;
        else if (a == 'X')
            return 10;
        else if (a == 'L')
            return 50;
        else if (a == 'C')
            return 100;
        else if (a == 'D')
            return 500;
        else if (a == 'M')
            return 1000;
        else 
            return -1;
    }
    int romanToInt(string s) {
        int n = s.length();
        int i = 0, result = 0, t, c;

        while (i < n) {
            if (i < n - 1 && (t = roman(s[i + 1])) > (c = roman(s[i]))){
                result += (t - c);
                i += 2;
            } else {
                result += roman(s[i]);
                i += 1;
            }
        }
        return result;
    }
};