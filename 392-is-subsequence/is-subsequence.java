class Solution {
    public boolean isSubsequence(String s, String t) {
        int temp = -1;
        for (char sc : s.toCharArray()) {
            int pos = t.indexOf(sc, temp + 1);
            if (pos == -1)
                return false;
            if (pos < temp)
                return false;
            temp = pos;
        }
        return true;
    }
}