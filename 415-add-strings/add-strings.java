class Solution {
    public String addStrings(String num1, String num2) {
        StringBuilder sb = new StringBuilder();
        int l1 = num1.length() - 1;
        int l2 = num2.length() - 1;
        int carry = 0;
        while (l1 >= 0 || l2 >= 0 || carry > 0) {
            int n1 = (l1 >= 0) ? num1.charAt(l1) - '0' : 0;
            int n2 = (l2 >= 0) ? num2.charAt(l2) - '0' : 0;
            int sum = n1 + n2 + carry;
            carry = sum / 10;
            sb.append(sum % 10);
            l1--; l2--;
        }
        return sb.reverse().toString();
    }
}