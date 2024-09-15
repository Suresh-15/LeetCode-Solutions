class Solution {
private:
    static bool IsDigit(char ch) { return (ch >= 48) && (ch <= 57); }

    static std::string StripLeadingZeroes(const std::string& str) {
        int index = 0;
        while ((index < str.size()) && (str[index] == '0'))
            ++index;

        std::string ans;
        for (int i = index; i < str.size(); ++i)
            ans.push_back(str[i]);

        if (ans.size() <= 0)
            return "0";

        return ans;
    }

public:
    int numDifferentIntegers(const std::string& word) {
        std::set<std::string> uniqueNums;
        std::string num;
        bool bNumFound = false;
        for (int i = 0; i < word.size(); ++i) {
            if (IsDigit(word[i])) {
                num.push_back(word[i]);
                bNumFound = true;
            } else if (bNumFound) {
                uniqueNums.insert(StripLeadingZeroes(num));
                num.clear();
                bNumFound = false;
            }
        }

        if (bNumFound)
            uniqueNums.insert(StripLeadingZeroes(num));

        return uniqueNums.size();
    }
};