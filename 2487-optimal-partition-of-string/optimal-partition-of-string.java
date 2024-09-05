class Solution {
    public int partitionString(String s) {
        List<String> al = new ArrayList<>();
        String temp = "";
        for (int i=0; i < s.length(); i++) {
            if (!temp.contains(String.valueOf(s.charAt(i))))
                temp = temp + String.valueOf(s.charAt(i));
            else {
                al.add(temp);
                temp = String.valueOf(s.charAt(i));
            }
        }
        al.add(temp);

        return al.size();
    }
}