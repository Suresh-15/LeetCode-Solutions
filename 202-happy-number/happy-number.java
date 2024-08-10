class Solution {
    public int sum_of_squares(int i) {
        int m, sqs = 0;
        while (i > 0) {
            m = i % 10;
            sqs += m * m;
            i = i / 10;
        }
        return sqs;
    }

    public boolean isHappy(int n) {
        int slow = n;
        int fast = n;

        do {
            slow = sum_of_squares(slow);
            fast = sum_of_squares(sum_of_squares(fast));
            if (slow == 1) {
                return true;
            }
        } while (slow != fast);
        return n == 1;
    }
}
