class Solution {
    public String shortestPalindrome(String s) {
        int index = 0;
        int length = s.length();
        for (int j = 0; j < length; j++) {
            if (s.charAt(index) == s.charAt(length - j - 1)) {
                index += 1;
            }
        }

        if (index == length) {
            return s;
        }

        StringBuilder t = new StringBuilder(s.substring(index, length));
        String p = t.reverse().toString();
        return p + shortestPalindrome(s.substring(0, index)) + s.substring(index);
    }
}