class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int length1 = s1.length();
        int length2 = s2.length();

        int[] s1_chars = new int[26];
        int[] s2_chars = new int[26];

        if (length1 > length2) {
            return false;
        }
        for (int i = 0; i < length1; i++) {
            s1_chars[s1.charAt(i) - 'a'] += 1;
            s2_chars[s2.charAt(i) - 'a'] += 1;
        }

        if (Arrays.compare(s1_chars, s2_chars) == 0) {
            return true;
        }

        for (int i = length1; i < length2; i++) {
            s2_chars[s2.charAt(i) - 'a'] += 1;
            s2_chars[s2.charAt(i - length1) - 'a'] -= 1;
            if (Arrays.compare(s1_chars, s2_chars) == 0) {
                return true;
            }
        }
        return false;
    }
}