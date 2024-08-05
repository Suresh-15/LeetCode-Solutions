class Solution {
public:
    string convert(string s, int numRows) {
        int n = s.length();
        if (numRows == 1 || numRows >= n)
            return s;
        string result;
        int len = 2 * numRows - 2;
        for (int i = 0; i < numRows; i++){
            for (int j = 0; i + j < n; j += len){
                result += s[i + j];
                if (i != 0 && i != numRows - 1 && j + len - i < n)
                    result += s[j + len - i];
            }
        }
        return result;
    }
};