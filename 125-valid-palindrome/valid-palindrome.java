class Solution {
    /*
     * public boolean isPalindrome(String s) {
     * StringBuilder word = new StringBuilder();
     * for (int i = 0; i < s.length(); i++) {
     * if (Character.isLetterOrDigit(s.charAt(i))) {
     * word.append(Character.toLowerCase(s.charAt(i)));
     * }
     * }
     * int n = word.length();
     * for (int i = 0; i < n / 2; i++) {
     * if (word.charAt(i) != word.charAt(n - 1 - i))
     * return false;
     * }
     * return true;
     * }
     */

    public boolean isPalindrome(String s) {
        int i = 0, j = s.length() - 1;
        while (i < j) {
            char iChar = s.charAt(i);
            char jChar = s.charAt(j);
            if (!isValid(iChar)) {
                i++;
            } else if (!isValid(jChar)) {
                j--;
            } else if (lower(iChar) != lower(jChar)) {
                return false;
            } else {
                i++;
                j--;
            }
        }
        return true;
    }

    boolean isValid(char c) {
        return (c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z') || (c >= '0' && c <= '9');
    }

    char lower(char c) {
        if (c >= 'A' && c <= 'Z') {
            return (char) (c + 32);
        }
        return c;
    }
}