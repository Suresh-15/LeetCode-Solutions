class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        int n = nums.length;
        List<Integer> numbers = new ArrayList<>();
        boolean[] present = new boolean[n + 1];

        for (int i = 0; i < n; i++) {
            present[nums[i]] = true;
        } 

        for (int i = 1; i <= n; i++) {
            if (!present[i]) {
                numbers.add(i);
            }
        }
        return numbers;
    }
}
