class Solution {
    public String compress(String s) {
        int count = 0;
        char prev = s.charAt(0);
        StringBuilder result = new StringBuilder("");

        for (int i = 0; i < s.length(); i++) {
            if (prev == s.charAt(i)) {
                count = count + 1;
            } else {
                result.append(count);
                result.append(s.charAt(i - 1));
                prev = s.charAt(i);
                count = 1;
            }
        }
        if (count != 0) {
            result.append(count);
            result.append(s.charAt(s.length() - 1));
        }

        return result.toString();
    }

    public String countAndSay(int n) {
        if (n == 1){
            return "1";
        }
        return compress(countAndSay(n - 1));
    }
}