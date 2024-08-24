class Solution {
    public int numeral(char r) {
        if (r == 'I')
            return 1;
        if (r == 'V')
            return 5;
        if (r == 'X')
            return 10;
        if (r == 'L')
            return 50;
        if (r == 'C')
            return 100;
        if (r == 'D')
            return 500;
        if (r == 'M')
            return 1000;
        return -1;
    }

    public int romanToInt(String s) {
        int result = 0;
        for (int i = 0; i < s.length(); i++) {
            int s1 = numeral(s.charAt(i));
            if (i + 1 < s.length()) {
                int s2 = numeral(s.charAt(i + 1));
                if (s1 >= s2) {
                    result = result + s1;
                } else {
                    result = result + (s2 - s1);
                    i++;
                }
            } else
                result = result + s1;
        }
        return result;

    }
}

/**
 * V = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
 * result, i, n = 0, 0, len(s)
 * while i < n:
 * if i < n - 1 and V[s[i]] < V[s[i + 1]]:
 * result += V[s[i + 1]] - V[s[i]]
 * i += 2
 * else:
 * result += V[s[i]]
 * i += 1
 * else:
 * return result
 */