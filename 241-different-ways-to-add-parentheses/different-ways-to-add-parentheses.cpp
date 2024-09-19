class Solution {
public:
    vector<int> diffWaysToCompute(string expression) {
        vector<int> result;
        for (int i = 0; i < expression.size(); ++i) {
            char oper = expression[i];
            if (oper == '+' || oper == '-' || oper == '*') {
                vector<int> s1 = diffWaysToCompute(expression.substr(0, i));
                vector<int> s2 = diffWaysToCompute(expression.substr(i + 1));
                for (int a : s1) {
                    for (int b : s2) {
                        if (oper == '+') 
                            result.push_back(a + b);
                        else if (oper == '-') 
                            result.push_back(a - b);
                        else if (oper == '*') 
                            result.push_back(a * b);
                    }
                }
            }
        }
        if (result.empty()) 
            result.push_back(stoi(expression));
        return result;
    }
};