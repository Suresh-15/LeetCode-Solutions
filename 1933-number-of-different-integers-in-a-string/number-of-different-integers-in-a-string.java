class Solution {
    public int numDifferentIntegers(String word) {
        StringBuffer sb = new StringBuffer(word);
        for (int i=0; i<word.length(); i++) {
            char ch = word.charAt(i);
            if (!Character.isDigit(ch)) sb.setCharAt(i, '\s');
        }

        String[] nums = sb.toString().split(" ");
        Set<String> st = new HashSet<>();
        for (int i=0; i<nums.length; i++) {
            if (!nums[i].trim().equals("")) {
                StringBuffer sb2 = new StringBuffer(nums[i].trim());
                int j =0;
                while (sb2.length() > 0) {
                    char ch = sb2.charAt(j);
                    if (ch != '0') break;
                    sb2.deleteCharAt(j);
                }

                st.add(sb2.toString());
            }
        }

        return st.size();
    }
}