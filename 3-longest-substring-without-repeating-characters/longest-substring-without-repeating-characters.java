class Solution {
    public int lengthOfLongestSubstring(String s) {
        int length = s.length();
        int maxLength = 0, left = 0;
        Set<Character> charset = new HashSet<>();

        for (int right = 0; right < length; right++) {
            if (!charset.contains(s.charAt(right))) {
                charset.add(s.charAt(right));
                maxLength = Math.max(maxLength, right - left + 1);
            } else {
                while (charset.contains(s.charAt(right))) {
                    charset.remove(s.charAt(left));
                    left++;
                }
                charset.add(s.charAt(right));
            }
        }
        return maxLength;
    }
}