class Solution {
    public String convertDateToBinary(String date) {
        int num1 = Integer.parseInt(date.substring(0, 4));
        int num2 = Integer.parseInt(date.substring(5, 7));
        int num3 = Integer.parseInt(date.substring(8, 10));

        StringBuilder sb = new StringBuilder();
        String strb1 = Integer.toBinaryString(num1);
        String strb2 = Integer.toBinaryString(num2);
        String strb3 = Integer.toBinaryString(num3);

        sb.append(strb1);
        sb.append("-");
        sb.append(strb2);
        sb.append("-");
        sb.append(strb3);

        return sb.toString();
    }
}