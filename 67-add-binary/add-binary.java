class Solution {
    public String addBinary(String a, String b) {
        StringBuilder result = new StringBuilder("");
        int carry = 0, i = a.length() - 1, j = b.length() - 1;

        while (i >= 0 || j >= 0 || carry == 1) {
            if (i >= 0)
                carry += a.charAt(i--) - '0';
            if (j >= 0) 
                carry += b.charAt(j--) - '0';

            result.append(carry % 2);
            carry = carry / 2;
        }
        return result.reverse().toString();
    }
}
