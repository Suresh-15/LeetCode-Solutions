class Solution {
public:
    double pow(double x, int n) {
        if (n == 0)
            return 1;
        n = abs(n);
        double temp = myPow(x, n / 2);
        if (n % 2 == 0)
            return temp * temp * 1.0;
        else
            return x * temp * temp * 1.0;
    }

    double myPow(double x, int n) {
        if (n > 0)
            return pow(x, n);
        return 1 / pow(x, n);
    }
};