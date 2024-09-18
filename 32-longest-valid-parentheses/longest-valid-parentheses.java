class Solution {
    public int longestValidParentheses(String s) {
        List<Integer> al = new ArrayList<>();
        int max_length = 0;
        al.add(-1);

        for (int idx = 0; idx < s.length(); idx++) {
            if (s.charAt(idx) == '(') {
                al.add(idx);
            } else {
                al.remove(al.size() - 1);
                if (al.size() == 0) {
                    al.add(idx);
                } else {
                    max_length = Math.max(max_length, idx - al.get(al.size() - 1));
                }
            }
        }
        return max_length;
    }
}