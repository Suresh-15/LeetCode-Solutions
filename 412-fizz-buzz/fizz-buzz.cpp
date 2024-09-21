class Solution {
public:
    vector<string> fizzBuzz(int n) {
        string str;
        vector<string> ans(n);
        for (int i = 1; i <= n; i++) {
            str = "";
            if (i % 3 == 0)
                str += "Fizz";
            if (i % 5 == 0)
                str += "Buzz";
            if (str == "")
                str = to_string(i);
            ans[i - 1] = str;
        }
        return ans;
    }
};