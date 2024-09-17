class Solution {
    public int getCommon(int[] nums1, int[] nums2) {
        if (nums1[nums1.length - 1] < nums2[0])
            return -1;
        if (nums2[nums2.length - 1] < nums1[0])
            return -1;

        int i = 0, j = 0;
        while (i < nums1.length && j < nums2.length) {
            if (nums1[i] == nums2[j])
                break;

            if (nums1[i] < nums2[j])
                i += 1;
            else if (nums1[i] > nums2[j])
                j += 1;
        }
        if (i == nums1.length || j == nums2.length)
            return -1;
        return nums1[i];
    }
}