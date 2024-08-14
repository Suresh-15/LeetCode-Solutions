class Solution {
    public int countSegments(String s) {
        int n = s.length();
        int count = 0, i = 0;
        while (i < n) {
            while (i < n && s.charAt(i) == ' ')
                i += 1;
            boolean add = false;
            while (i < n && s.charAt(i) != ' ') {
                i += 1;
                add = true;
            }
            if (add)
                count += 1;
        }
        return count;
    }
}