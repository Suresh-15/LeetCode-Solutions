class Solution {
    public int majorityElement(int[] nums) {
        int count = 0, element = nums[0];
        for (int i = 0; i < nums.length; i++) {
            if (count == 0) {
                element = nums[i];
            }

            if (nums[i] == element) {
                count += 1;
            } else {
                count -= 1;
            }
        }
        return element;
    }
}