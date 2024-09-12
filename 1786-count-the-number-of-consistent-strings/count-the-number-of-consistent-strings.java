class Solution {
    public int countConsistentStrings(String allowed, String[] words) {
        int count = 0;
        for (int i = 0; i < words.length; i++) {
            String word = words[i];
            for (int j = 0; j < word.length(); j++) {
                if (!allowed.contains(String.valueOf(word.charAt(j)))) {
                    count += 1;
                    break;
                }
            }
        }
        return words.length - count;
    }
}