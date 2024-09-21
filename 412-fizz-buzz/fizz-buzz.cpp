class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> result;
        string fizz = "Fizz", buzz = "Buzz";
        for (int i = 1; i <= n; i++) {
            if (i % 3 == 0 && i % 5 == 0) {
                result.push_back(fizz + buzz);
            } else if (i % 3 == 0) {
                result.push_back(fizz);
            } else if (i % 5 == 0) {
                result.push_back(buzz);
            } else {
                result.push_back(to_string(i));
            }
        }
        return result;
    }
};