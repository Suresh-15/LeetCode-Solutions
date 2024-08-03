class Solution {
public:
    string addBinary(string a, string b) {
        int gap = a.length() - b.length();
        if (gap < 0) {
            string c = b;
            b = a;
            a = c;
            gap = -1 * gap;
        }

        for (int i = 0; i < gap; i++) {
            b = '0' + b;
        }

        bool carry = false;
        string result = "";
        for (int i = a.length() - 1; i >= 0; i--) {
            if (a[i] == '1' && b[i] == '1') {
                result = (carry ? '1' : '0') + result;
                carry = true;
            } else if (a[i] == '0' && b[i] == '0') {
                result = (carry ? '1' : '0') + result;
                carry = false;
            } else {
                result = (carry ? '0' : '1') + result;
            }
        }

        if (carry)
            result = '1' + result;
        return result;
    }
};