class Solution {
    public int[] arrayRankTransform(int[] arr) {
        if (arr.length == 0) {
            return arr;
        }
        int[] nums = arr.clone();
        Arrays.sort(nums);
        HashMap<Integer, Integer> ranks = new HashMap<>();
        int rank = 1;
        ranks.put(nums[0], rank++);

        for (int i = 1; i < arr.length; i++) {
            if (nums[i] == nums[i - 1]) {
                continue;
            } else {
                ranks.put(nums[i], rank++);
            }
        }
        
        for (int i = 0; i < arr.length; i++) {
            nums[i] = ranks.get(arr[i]);
        }
        
        return nums;
    }
}