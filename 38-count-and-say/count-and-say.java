class Solution {
    public String compress(String s) {
        int count = 0;
        char prev = s.charAt(0);
        String result = "";

        for (int i = 0; i < s.length(); i++) {
            if (prev == s.charAt(i)) {
                count = count + 1;
            } else {
                result = result + String.valueOf(count) + s.charAt(i - 1);
                prev = s.charAt(i);
                count = 1;
            }
        }
        if (count != 0) {
            result = result + String.valueOf(count) + s.charAt(s.length() - 1);
        }

        return result;
    }

    public String countAndSay(int n) {
        if (n == 1){
            return "1";
        }
        return compress(countAndSay(n - 1));
    }
}