class Solution {
public:
    int minBitFlips(int start, int goal) {
        int count = 0;
        while (start > 0 || goal > 0) {
            int bitStart = (start & 1);
            int bitGoal = (goal & 1);
            count += (bitStart != bitGoal) ? 1 : 0;
            start = (start > 0) ? start >> 1 : 0;
            goal = (goal > 0) ? goal >> 1 : 0;
        }

        return count;   
    }
};