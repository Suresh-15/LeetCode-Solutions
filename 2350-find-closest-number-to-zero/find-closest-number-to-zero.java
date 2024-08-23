class Solution {
    public int findClosestNumber(int[] nums) {
        int ans = nums[0];
        for (int num : nums) {
            if (Math.abs(num) <= Math.abs(ans)) {
                if (Math.abs(num) == Math.abs(ans))
                    ans = (num > ans) ? num : ans;
                else
                    ans = num;
            }
        }
        return ans;
    }
}