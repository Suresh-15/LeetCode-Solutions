class Solution {
    public int thirdMax(int[] nums) {
        
        List<Integer> al = new ArrayList<>();
        for (int i=0; i<nums.length; i++) {
            if (!al.contains(nums[i]))
                al.add(nums[i]);
        }
        if (al.size() <= 2){
            return Collections.max(al);
        }

        int least = Integer.MIN_VALUE;
        int first = least, second = least, third = least;
        for (int i : al) {
            if (i > first){
                third = second;
                second = first;
                first = i;
            } else if (i > second) {
                third = second;
                second = i;
            } else if (i > third) {
                third = i;
            }
        }
        return third;
    }
}