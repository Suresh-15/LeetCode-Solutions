class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string result = "";
        int minIndex = min(word1.length(), word2.length());
        for (int i = 0; i < minIndex; i++) {
            result += word1[i];
            result += word2[i];
        }
        if (word1.length() < word2.length()) {
            for (int i = minIndex; i < word2.length(); i++)
                result += word2[i];
        } else if (word2.length() < word1.length()) {
            for (int i = minIndex; i < word1.length(); i++)
                result += word1[i];
        }
        return result;
    }
};