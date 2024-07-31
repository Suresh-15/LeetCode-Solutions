class Solution {
    public int[] twoSum(int[] nums, int target) {

        int[] result = new int[2];
        Map<Integer, Integer> seen = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (seen.containsKey(complement) == true) {
                result[0] = i;
                result[1] = seen.get(complement);
                return result;
            }
            seen.put(nums[i], i);
        }
        return result;
    }
}
