class Solution {
    public char kthCharacter(int k) {
        char result = 'a';
        k -= 1;
        while (k > 0) {
            result = (char) (result + (k % 2));
            if (result == 123) {
                result = 'a';
            }
            k /= 2;
        }
        return result;
    }
}