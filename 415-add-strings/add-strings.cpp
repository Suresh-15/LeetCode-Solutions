class Solution {
public:
    int charToInt(char s){
        return s - '0';
    }

    char intToChar(int a){
        return a + '0';
    }

    string addStrings(string num1, string num2) {
        if (num1.length() > num2.length())
            swap(num1, num2);

        reverse(num1.begin(), num1.end());
        reverse(num2.begin(), num2.end());
        string result = "";
        int carry = 0;

        for (int i = 0; i < num1.length(); i++) {
            int a = charToInt(num1[i]);
            int b = charToInt(num2[i]);
            int sum = a + b + carry;
            int ans = sum % 10;
            carry = sum / 10;
            result += intToChar(ans);
        }

        for (int i = num1.length(); i < num2.length(); i++) {
            int a = charToInt(num2[i]);
            int sum = a + carry;
            int ans = sum % 10;
            carry = sum / 10;
            result += intToChar(ans);
        }
        if (carry)
            result += "1";
        reverse(result.begin(), result.end());

        return result;
    }
};