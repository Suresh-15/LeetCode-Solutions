class Solution {
    List<List<Integer>> result;

    private void backtrack(int[] nums, int start) {
        if (start == nums.length - 1) {
            List<Integer> x = new ArrayList<Integer>();
            for (int i : nums) {
                x.add(i);
            }
            result.add(x);
        }
        for (int i = start; i < nums.length; i++) {
            int temp = nums[start];
            nums[start] = nums[i];
            nums[i] = temp;
            backtrack(nums, start + 1);
            temp = nums[start];
            nums[start] = nums[i];
            nums[i] = temp;
        }
    }

    public List<List<Integer>> permute(int[] nums) {
        result = new ArrayList<>();
        backtrack(nums, 0);
        return result;

    }
}
