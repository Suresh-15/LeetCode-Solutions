class Solution {
public:
    int sum_of_digits(int i){
        int result = 0;
        while (i > 0){
            result += i % 10;
            i /= 10;
        }
        return result;
    }

    int addDigits(int num) {
        while (num / 10 != 0){
            num = sum_of_digits(num);
        }
        return num;
    }
};