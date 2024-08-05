class Solution {
    public String convert(String s, int numRows) {
        /**
         * List<Character>[] al = new ArrayList[numRows];
         * if (numRows == 1 || numRows >= s.length())
         * return s;
         * 
         * for(int i=0; i < numRows; i++)
         * al[i] = new ArrayList<>();
         * 
         * int index = 0, zigzag = 0;
         * for (char x: s.toCharArray()){
         * al[index].add(x);
         * if (index == numRows - 1)
         * zigzag = -1;
         * else if (index == 0)
         * zigzag = 1;
         * index += zigzag;
         * }
         * 
         * StringBuilder result = new StringBuilder();
         * for (List<Character> m: al){
         * for (char c: m){
         * result.append(c);
         * }
         * }
         * 
         * return result.toString();
         * 
         */

        if (numRows == 1 || s.length() < numRows) {
            return s;
        }

        int len = s.length();
        char[] result = new char[len];
        int diff = (numRows - 1) * 2;
        int count = 0;
        int i = 0;

        while (i < numRows) {
            int temp = i;
            while (count < len && temp < len) {
                result[count++] = s.charAt(temp);
                if (i == 0 || i == (numRows - 1)) {
                    temp += diff;
                } else {
                    temp += diff - i * 2;
                    if (temp < len) {
                        result[count++] = s.charAt(temp);
                        temp += i * 2;
                    }
                }
            }
            i++;
        }
        return new String(result);
    }
}