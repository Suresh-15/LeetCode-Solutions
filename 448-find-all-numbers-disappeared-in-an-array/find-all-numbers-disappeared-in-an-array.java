class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        List<Integer> numbers = new ArrayList<>();
        boolean[] present = new boolean[nums.length + 1];
        for (int i = 0; i < nums.length; i++) {
            present[nums[i]] = true;
        } 
        for (int i = 1; i <= nums.length; i++) {
            if (!present[i]) {
                numbers.add(i);
            }
        }
        return numbers;
    }
}
