class Solution {
public:
    int getCommon(vector<int>& nums1, vector<int>& nums2) {
        int l1 = nums1.size(), l2 = nums2.size();
        if (nums1.back() < nums2.front())
            return -1;
        if (nums2.back() < nums1.front())
            return -1;

        int i = 0, j = 0;
        while (i < l1 && j < l2) {
            if (nums1[i] == nums2[j])
                break;

            if (nums1[i] < nums2[j])
                i += 1;
            else if (nums1[i] > nums2[j])
                j += 1;
        }
        if (i == l1 || j == l2)
            return -1;
        return nums1[i];
    }
};