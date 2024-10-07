class Solution {
    public int minLength(String s) {
        char[] stack = new char[s.length() + 1];
        int top = -1;
        for (char c : s.toCharArray()) {
            if (top > -1 && (c == 'B' && stack[top] == 'A' || c == 'D' && stack[top] == 'C')) {
                top--;
            } else {
                top++;
                stack[top] = c;
            }
        }
        return top + 1;
    }
}