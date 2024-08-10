class Solution {
    public int sum_of_digits(int i) {
        int sod = 0;
        while (i > 0) {
            sod += i % 10;
            i /= 10;
        }
        return sod;
    }

    public int addDigits(int num) {
        while (num / 10 != 0) {
            num = sum_of_digits(num);
        }
        return num;
    }
}