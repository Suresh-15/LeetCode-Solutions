class Solution {
public:
    vector<int> lexicalOrder(int n) {
        int num = 1;
        vector<int> lexOrderList;
        for (int i = 0; i < n; i++) {
            lexOrderList.push_back(num);
            if (num * 10 <= n) {
                num *= 10;
            } else {
                while (num % 10 == 9 || num + 1 > n) {
                    num /= 10;
                }
                num += 1;
            }
        }
        return lexOrderList;        
    }
};