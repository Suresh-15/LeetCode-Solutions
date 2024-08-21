class Solution {
    public int lengthOfLongestSubstring(String s) {
        int[] map = new int[128];
        int max = 0;
        int j = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (map[c] > 0) {
                j = Math.max(j, map[c]);
            }
            map[c] = i + 1;
            max = Math.max(max, i - j + 1);
        }
        return max;
    }
}