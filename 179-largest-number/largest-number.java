import java.util.Arrays;
import java.util.Comparator;

class Solution {
    public String largestNumber(int[] nums) {
        String[] numbers = new String[nums.length];
        for (int i = 0; i < nums.length; i++)
            numbers[i] = String.valueOf(nums[i]);

        Comparator<String> compare = (x, y) -> {
            String xy = x + y;
            String yx = y + x;
            return yx.compareTo(xy);
        };

        Arrays.sort(numbers, compare);
        StringBuilder sb = new StringBuilder();
        for (String i : numbers)
            sb.append(i);
        return sb.charAt(0) == '0' ? "0" : sb.toString();
    }
}