class Solution {
    void backtrack(List<String> res, StringBuilder curr, int open, int close, int n) {
        if (curr.length() == 2 * n) {
            res.add(curr.toString());
        }
        if (open < n) {
            curr.append('(');
            backtrack(res, curr, open + 1, close, n);
            curr.deleteCharAt(curr.length() - 1);
        }
        if (close < open) {
            curr.append(')');
            backtrack(res, curr, open, close + 1, n);
            curr.deleteCharAt(curr.length() - 1);
        }
    }

    public List<String> generateParenthesis(int n) {
        List<String> res = new ArrayList<>();
        backtrack(res, new StringBuilder(""), 0, 0, n);
        return res;
    }
}