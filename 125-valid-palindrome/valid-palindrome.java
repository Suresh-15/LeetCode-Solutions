class Solution {
    public boolean isPalindrome(String s) {
        StringBuilder word = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            if (Character.isLetterOrDigit(s.charAt(i))) {
                word.append(Character.toLowerCase(s.charAt(i)));
            }
        }
        int n = word.length();
        for (int i = 0; i < n / 2; i++) {
            if (word.charAt(i) != word.charAt(n - 1 - i))
                return false;
        }
        return true;
    }
}