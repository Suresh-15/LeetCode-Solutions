class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> result = new ArrayList<>();
        List<String> output = new ArrayList<>();
        backtrack(n, 0, 0, output, result);
        return result;
    }

    public void backtrack(int n, int leftCount, int rightCount, List<String> output, List<String> result) {
        if (leftCount >= n && rightCount >= n) {
            String outputStr = String.join("", output);
            result.add(outputStr);
        }

        if (leftCount < n) {
            output.add("(");
            backtrack(n, leftCount + 1, rightCount, output, result);
            output.remove(output.size() - 1);
        }
        if (rightCount < leftCount) {
            output.add(")");
            backtrack(n, leftCount, rightCount + 1, output, result);
            output.remove(output.size() - 1);
        }
    }
}