class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1 || numRows >= s.length()) {
            return s;
        }

        int index = 0, zigzag = 0;
        vector<vector<char>> v(numRows);
        for (int i = 0; i < s.length(); i++) {
            v[index].push_back(s[i]);
            if (index == numRows - 1)
                zigzag = -1;
            else if (index == 0)
                zigzag = 1;
            index += zigzag;
        }

        string result;
        for(const auto& m: v){
            for(char c: m)
                result += c;
        }

        return result;
    }
};