class Solution {
    public int[] missingRolls(int[] rolls, int mean, int n) {
        int[] second_list = new int[] {};
        int total_elements = rolls.length + n;
        int sum_of_all_elements = mean * total_elements;
        int sum_of_first_list = 0;
        for (int i : rolls)
            sum_of_first_list += i;
        int sum_of_second_list = sum_of_all_elements - sum_of_first_list;

        if (sum_of_second_list < n || sum_of_second_list > 6 * n)
            return second_list;

        second_list = new int[n];
        Arrays.fill(second_list, 1);
        /*
         * for (int i = 0; i < n; i++)
         * second_list[i] = 1;
         */

        sum_of_second_list -= n;
        for (int i = 0; i < n; i++) {
            second_list[i] += Math.min(5, sum_of_second_list);
            sum_of_second_list -= 5;
            if (sum_of_second_list <= 0)
                break;
        }

        return second_list;

    }
}