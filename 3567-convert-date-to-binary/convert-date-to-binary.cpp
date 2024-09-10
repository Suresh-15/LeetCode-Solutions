class Solution {
public:
    string bin (int num) {
        string result = "";
        while (num > 0) {
            result = to_string(num % 2) + result;
            num = num / 2;
        }
        return result;
    }
    string convertDateToBinary(string date) {
        string y = date.substr(0, 4);
        string m = date.substr(5, 2);
        string d = date.substr(8, 2);
        return bin(stoi(y)) + "-" + bin(stoi(m)) + "-" + bin(stoi(d));
    }
};