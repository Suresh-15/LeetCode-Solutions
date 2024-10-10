class Solution {
public:
    char kthCharacter(int k) {
        string ans = "a";
        while (ans.length() < k) {
            string temp = "";
            for (char c : ans) {
                if (c == 'z') {
                    temp.push_back('a');
                } else {
                    temp.push_back(c + 1);
                }
            }
            ans += temp;
        }
        return ans[k - 1];
    }
};