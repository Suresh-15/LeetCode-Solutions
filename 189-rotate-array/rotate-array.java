class Solution {
    public void rotate(int[] nums, int k) {
        int length = nums.length;
        int[] rotated = new int[length];
        for (int i = 0; i < length; i++)
            rotated[(i + k) % length] = nums[i];
        for (int i = 0; i < length; i++)
            nums[i] = rotated[i];
    }
}