class Solution {
    public int sum_of_squares(int i) {
        int m, sqs = 0;
        while (i > 0) {
            m = i % 10;
            sqs += Math.pow(m, 2);
            i = i / 10;
        }
        return sqs;
    }

    public boolean isHappy(int n) {
        ArrayList<Integer> al = new ArrayList<>();
        while (n > 1) {
            if (al.contains(n))
                return false;
            al.add(n);
            n = sum_of_squares(n);
        }
        return n == 1;
    }
}
