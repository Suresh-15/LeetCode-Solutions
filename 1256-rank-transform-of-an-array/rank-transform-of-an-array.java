class Solution {
    
    public int[] sort_and_unique(int[] arr) {
        Set<Integer> set = new HashSet<>();
        for(int num : arr) {
            set.add(num);
        }    
        int[] nums = set.stream().mapToInt(Integer :: intValue).toArray();
        Arrays.sort(nums);
        return nums;
    }

    public int[] arrayRankTransform(int[] arr) {
        int[] nums = sort_and_unique(arr);
        Map<Integer, Integer> map = new HashMap<>();
        int rank = 1;
        for (int num : nums) {
            map.put(num, rank++);
        }
        int[] ranks = new int[arr.length];
        for (int i = 0; i < arr.length; i++) {
            ranks[i] = map.get(arr[i]);
        }
        return ranks;
    }
}