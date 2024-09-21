class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> result;
        string fizz = "Fizz", buzz = "Buzz", add;
        for (int i = 1; i <= n; i++) {
            add = "";
            if (i % 3 == 0) {
                add += fizz;
            }
            if (i % 5 == 0) {
                add += buzz;
            }
            if (add == "") {
                add = to_string(i);
            }
            result.push_back(add);
        }
        return result;
    }
};