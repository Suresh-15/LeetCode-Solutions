class Solution {
    public int minSwaps(String s) {
        int top = -1, unbalanced = 0;
        for (char bracket : s.toCharArray()) {
            if (bracket == '[') {
                top += 1;
            } else {
                if (top == -1) {
                    unbalanced += 1;
                } else {
                    top -= 1;
                }
            }
        }
        int swaps = (unbalanced + 1) / 2;
        return swaps;
    }
}