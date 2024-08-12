class Solution {
public:
    int thirdMax(vector<int>& nums) {
        set<int> s;
        bool f = 0;
        for (int i : nums) {
            if (i == -2147483648)
                f = 1;
            s.insert(i);
        }

        if (s.size() == 2) {
            int a = INT_MIN;
            for (int i : s)
                a = i;
            return a;
        }

        int max1 = INT_MIN, max2 = INT_MIN, max3 = INT_MIN;
        for (int i : s) {
            if (i > max1) {
                max3 = max2;
                max2 = max1;
                max1 = i;
            } else if (i < max1 and i > max2) {
                max3 = max2;
                max2 = i;
            } else if (i < max2 and i > max3)
                max3 = i;
        }

        if (max3 == -2147483648 and f == 0)
            return max1;
        return max3;
    }
};