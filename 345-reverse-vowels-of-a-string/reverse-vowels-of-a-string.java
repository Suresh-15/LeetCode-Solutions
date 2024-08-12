class Solution {
    public boolean isVowel(char a) {
        if (a == 'a' || a == 'e' || a == 'i' || a == 'o' || a == 'u'
                || a == 'A' || a == 'E' || a == 'I' || a == 'O' || a == 'U') {
            return true;
        } else {
            return false;
        }
    }

    public String reverseVowels(String s) {
        char[] letters = s.toCharArray();
        int l = 0, r = letters.length - 1;
        boolean left = false, right = false;
        while (l <= r) {
            left = isVowel(letters[l]);
            right = isVowel(letters[r]);
            if (left && right) {
                char temp = letters[l];
                letters[l] = letters[r];
                letters[r] = temp;
                l++;
                r--;
            } else if (!left) {
                l++;
            } else if (!right) {
                r--;
            }
        }
        return new String(letters);
    }
}