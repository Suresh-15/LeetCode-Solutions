class Solution {
public:
    void backtrack(int n, int leftCount, int rightCount, vector<char>& output,
                   vector<string>& result) {
        if (leftCount >= n && rightCount >= n) {
            string outputStr(output.begin(), output.end());
            result.push_back(outputStr);
        }
        if (leftCount < n) {
            output.push_back('(');
            backtrack(n, leftCount + 1, rightCount, output, result);
            output.pop_back();
        }
        if (rightCount < leftCount) {
            output.push_back(')');
            backtrack(n, leftCount, rightCount + 1, output, result);
            output.pop_back();
        }
    }
    vector<string> generateParenthesis(int n) {
        vector<string> result;
        vector<char> output;
        backtrack(n, 0, 0, output, result);
        return result;
    }
};
