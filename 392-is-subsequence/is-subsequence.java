class Solution {
    public boolean isSubsequence(String s, String t) {
        int ptr = 0, n = s.length();
        for (int i = 0; i < t.length(); i++) {
            if (ptr < n && s.charAt(ptr) == t.charAt(i)) {
                ptr += 1;
            } else if (ptr == n) {
                return true;
            }

        }
        if (ptr == n) {
            return true;
        } else {
            return false;
        }
    }
}