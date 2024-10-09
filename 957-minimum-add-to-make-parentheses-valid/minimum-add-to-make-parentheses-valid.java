class Solution {
    public int minAddToMakeValid(String s) {
        int min_count = 0; 
        int open_deficit = 0;

        for (char c: s.toCharArray()) { 
            if (c == '(') {
                open_deficit += 1;
            } else {
                if (open_deficit == 0) {
                    min_count += 1;
                } else {
                    open_deficit -= 1;
                }
            }
        }
        return min_count + open_deficit;
    }
}