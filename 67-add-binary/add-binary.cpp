class Solution {
public:
    string addBinary(string a, string b) {
        string c(max(a.size(), b.size()) + 1, '0');
        int ai = (int)a.size() - 1;
        int bi = (int)b.size() - 1;
        int ci = (int)c.size() - 1;
        int carry = 0;

        while (ci >= 0) {
            int sum = 0;
            if (ai >= 0 && a[ai] == '1') {
                ++sum;
            }
            if (bi >= 0 && b[bi] == '1') {
                ++sum;
            }
            sum += carry;

            if (sum % 2 == 1) {
                c[ci] = '1';
            }
            carry = (sum > 1) ? 1 : 0;

            --ai;
            --bi;
            --ci;
        }

        if (c[0] == '0') {
            c.erase(c.begin());
        }

        return c;
    }
};