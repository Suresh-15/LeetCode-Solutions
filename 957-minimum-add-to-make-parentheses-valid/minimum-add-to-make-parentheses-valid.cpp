class Solution {
public:
    int minAddToMakeValid(string s) {
        int res = 0;
        int numOpen = 0;
        for (char c : s) {
            if (c == '(') {
                ++numOpen;
            } else {
                numOpen > 0 ? numOpen-- : res++;
            }
        }
        return numOpen + res;
    }
};