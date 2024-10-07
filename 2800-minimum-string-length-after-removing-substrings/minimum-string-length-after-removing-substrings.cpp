class Solution {
public:
    int minLength(string s) {
        char stack[s.length() + 1];
        int top = -1;

        for (int i = 0; i < s.length(); i++) {
            char current = s[i];
            if (top > -1 && ((current == 'B' && stack[top] == 'A') || (current == 'D' && stack[top] == 'C'))) {
                top--;
            } else {
                stack[++top] = current;
            }
        }
        return top + 1;
    }
};