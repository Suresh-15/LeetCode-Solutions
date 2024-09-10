class Solution {
    public String bin(int num) {
        StringBuilder s = new StringBuilder();
        while (num > 0) {
            s.append(String.valueOf(num % 2));
            num = num / 2;
        }
        s.reverse();
        return s.toString();
    }
    public String convertDateToBinary(String date) {
        int y = Integer.parseInt(date.substring(0, 4));
        int m = Integer.parseInt(date.substring(5, 7));
        int d = Integer.parseInt(date.substring(8));

        return bin(y) + "-" + bin(m) + "-" + bin(d);
    }
}