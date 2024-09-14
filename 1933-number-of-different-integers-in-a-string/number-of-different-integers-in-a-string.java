class Solution {
    public int numDifferentIntegers(String word) {
        Set<String> s = new HashSet<>();
        int n = word.length();
        int ind = 0;
        boolean v = false;
        for (int i = 0; i < n; i++) {
            char ch = word.charAt(i);
            if (ch >= '0' && ch <= '9') {
                if (!v) 
                    ind = i;
                v = true;
            } else {
                if (v) {
                    while (word.charAt(ind) == '0') 
                        ind++;
                    s.add(word.substring(ind, i));
                }
                v = false;
            }
        }
        if (v) {
            while (ind < n && word.charAt(ind) == '0') 
                ind++;
            s.add(word.substring(ind));
        }
        return s.size();
    }
}