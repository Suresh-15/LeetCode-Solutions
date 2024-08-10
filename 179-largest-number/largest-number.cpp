class Solution {
public:
    string largestNumber(vector<int>& nums) {
        vector<string> numbers;
        for (int num : nums)
            numbers.push_back(to_string(num));

        auto compare = [](const string& x, const string& y) {
            string xy = x + y;
            string yx = y + x;
            return xy > yx;
        };

        sort(numbers.begin(), numbers.end(), compare);
        string result;
        for (string t : numbers)
            result += t;
        return result[0] == '0' ? "0" : result;
    }
};