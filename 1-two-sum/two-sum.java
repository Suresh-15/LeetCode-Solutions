class Solution {
    public int[] twoSum(int[] nums, int target) {

        int[] result = new int[2];
        Map<Integer, Integer> seen = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            for (Map.Entry<Integer, Integer> m : seen.entrySet()) {
                if (m.getKey() == complement) {
                    result[0] = m.getValue();
                    result[1] = i;
                    return result;
                }
            }
            seen.put(nums[i], i);
        }
        return result;
    }
}
