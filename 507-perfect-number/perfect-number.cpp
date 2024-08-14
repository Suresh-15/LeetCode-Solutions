class Solution {
public:
    bool checkPerfectNumber(int num) {
        if (num == 1)
            return false;
        int answer = 1, i = 2;
        while (i * i < num) {
            if (num % i == 0)
                answer += i + num / i;
            i += 1;
        }
        if (i * i == num)
            answer += i;

        return answer == num;
    }
};