class Solution {
    public String convertDateToBinary(String date) {
        int y = Integer.parseInt(date.substring(0, 4));
        int m = Integer.parseInt(date.substring(5, 7));
        int d = Integer.parseInt(date.substring(8));

        String d1 = String.valueOf(Integer.toBinaryString(d));
        String m1 = String.valueOf(Integer.toBinaryString(m));
        String y1 = String.valueOf(Integer.toBinaryString(y));
    
        return y1 + "-" + m1 + "-" + d1;
    }
}