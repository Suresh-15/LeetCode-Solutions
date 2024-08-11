class Solution {
    public boolean containsDuplicate(int[] nums) {
        for (int i = 1; i < nums.length; i++) {
            int j = i;
            int ele = nums[j];
            j--;
            for (; j >= 0 && ele < nums[j]; j--) {
                nums[j + 1] = nums[j];
            }
            nums[j + 1] = ele;
            if (j >= 0 && j < nums.length - 1 && nums[j] == nums[j + 1])
                return true;
        }
        return false;
    }
}