class Solution {
public:

    bool check(string word, bool allowed[]) {
        for (int i = 0; i < word.length(); i++) {
            if (allowed[word[i] - 'a'])
                continue;
            else
                return false;
        }
        return true;
    }

    int countConsistentStrings(string allowed, vector<string>& words) {
        bool allowed_chars[26];
        for (int i = 0; i < allowed.length(); i++) 
            allowed_chars[allowed[i] - 'a'] = true;

        int result = 0;
        for (int i = 0; i < words.size(); i++) {
            if (check(words[i], allowed_chars))
                result += 1;
        }
        return result;
    }
};