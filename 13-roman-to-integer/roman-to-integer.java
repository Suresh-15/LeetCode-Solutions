class Solution {
    public int romanToInt(String s) {
        HashMap<Character, Integer> V = new HashMap<Character, Integer>();
        V.put('I', 1);  V.put('V', 5);  V.put('X', 10);
        V.put('L', 50); V.put('C', 100); V.put('D', 500);
        V.put('M', 1000);

        int result = 0, i = 0, n = s.length();
        while (i < n) {
            if (i < n - 1 && V.get(s.charAt(i + 1)) > V.get(s.charAt(i))) {
                result += (V.get(s.charAt(i + 1)) - V.get(s.charAt(i)));
                i += 2;
            } else {
                result += V.get(s.charAt(i));
                i += 1;
            }
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