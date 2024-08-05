class Solution {
    public String convert(String s, int numRows) {
        List<Character>[] al = new ArrayList[numRows];
        if (numRows == 1 || numRows >= s.length())
            return s;

        for(int i=0; i < numRows; i++)
            al[i] = new ArrayList<>();

        int index = 0, zigzag = 0;
        for (char x: s.toCharArray()){
            al[index].add(x);
            if (index == numRows - 1)
                zigzag = -1;
            else if (index == 0)
                zigzag = 1;
            index += zigzag;
        }

        StringBuilder result = new StringBuilder();
        for (List<Character> m: al){
            for (char c: m){
                result.append(c);
            }
        }

        return result.toString();
    }
}