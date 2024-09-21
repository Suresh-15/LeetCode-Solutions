class Solution {
    public List<String> fizzBuzz(int n) {
        String str;
        List<String> result = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            str = "";
            if (i % 3 == 0)
                str += "Fizz";
            if (i % 5 == 0)
                str += "Buzz";
            if (str == "")
                str = String.valueOf(i);
            result.add(str);
        }
        return result;
    }
}