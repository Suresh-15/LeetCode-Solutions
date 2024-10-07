class Solution {
    public boolean areSentencesSimilar(String sentence1, String sentence2) {
        String first = sentence1;
        String second = sentence2;
        if (first.length() == second.length()) {
            return first.equals(second);
        }
        if (sentence2.length() < first.length()) {
            first = sentence2;
            second = sentence1;
        }
        int i = -1;
        while (i + 1 < first.length() && first.charAt(i + 1) == second.charAt(i + 1)) {
            i++;
        }
        int j = first.length();
        int last = second.length();
        while (j - 1 >= 0 && first.charAt(j - 1) == second.charAt(last - 1)) {
            j--;
            last--;
        }

        if (i == first.length() - 1 && second.charAt(i + 1) == ' ') {
            return true;
        }
        if (j == 0 && second.charAt(last - 1) == ' ') {
            return true;
        }
        if (i + 1 >= j && second.charAt(i) == ' ' && second.charAt(last) == ' ') {
            return true;
        }

        return false;
    }
}