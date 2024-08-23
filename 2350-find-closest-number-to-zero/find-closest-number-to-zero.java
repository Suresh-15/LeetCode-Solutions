class Solution {
    public int findClosestNumber(int[] nums) {
        int min = Integer.MAX_VALUE;
        int minindex = 0;
        for (int i = 0; i < nums.length; i++) {
            if (Math.abs(nums[i]) < min) {
                min = Math.abs(nums[i]);
                minindex = i;
            }
            
            if (min == nums[i])
                if (minindex < i)
                    minindex = i;
        }
        return nums[minindex];
    }
}