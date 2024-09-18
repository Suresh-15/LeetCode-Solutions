class Solution {
    public int[] productExceptSelf(int[] nums) {
        boolean zeros = false;
        int count = 0, product = 1;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) {
                count += 1;
                zeros = true;
            } else {
                product *= nums[i];
            }
        }

        if (count > 1) {
            return new int[nums.length];
        }

        int[] result = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) {
                result[i] = product;
            } else {
                if (zeros) {
                    result[i] = 0;
                } else {
                    result[i] = product / nums[i]; 
                }
            }
        }

        return result;
    }
}