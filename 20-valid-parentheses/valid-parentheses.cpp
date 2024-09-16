class Solution {
public:
    bool isValid(string s) {
        vector<char> opens;
        if (s.length() % 2 != 0)
            return false;
        
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '(' || s[i] == '{' || s[i] == '[')
                opens.push_back(s[i]);
            else {
                if (opens.size() == 0)
                    return false;
                
                char character = opens.back();
                opens.pop_back();
                if (
                    (character == '{' && s[i] != '}') ||
                    (character == '[' && s[i] != ']') ||
                    (character == '(' && s[i] != ')')
                )
                    return false;
            }
        }

        if (opens.size() != 0)
            return false;
        return true;

    }
};