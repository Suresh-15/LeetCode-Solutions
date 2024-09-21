class Solution {
    public List<Integer> lexicalOrder(int n) {
        int num = 1;
        List<Integer> al = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            al.add(num);
            if (num * 10 <= n) {
                num *= 10;
            } else {
                while (num % 10 == 9 || num + 1 > n) {
                    num /= 10;
                }
                num += 1;
            }
        }
        return al;
    }
}