class Solution {
    public char kthCharacter(int k) {
        String str = "a";
        while (str.length() < k) {
            StringBuilder temp = new StringBuilder();
            for (char c : str.toCharArray()) {
                if (c == 'z') {
                    temp.append('a');
                } else {
                    temp.append((char) (c + 1));
                }
            }
            str += temp.toString();
        }
        return str.charAt(k - 1);
    }
}