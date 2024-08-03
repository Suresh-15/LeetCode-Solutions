class Solution {
public:
    string addBinary(string a, string b) {
        string str;
        int m = a.length() - 1;
        int n = b.length() - 1;
        int carry = 0;

        while (m >= 0 || n >= 0) {
            int sum = carry;
            if (m >= 0)
                sum += a[m--] - '0';
            if (n >= 0)
                sum += b[n--] - '0';

            carry = sum > 1 ? 1 : 0;
            str += to_string(sum % 2);
        }
        if (carry)
            str += to_string(carry);
        reverse(str.begin(), str.end());
        return str;
    }
};