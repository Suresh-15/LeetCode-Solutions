class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals,
                               vector<int>& newInterval) {

        vector<vector<int>> result;
        int newStart = newInterval[0];
        int newEnd = newInterval[1];
        int i = 0, n = intervals.size();

        while (i < n && newStart > intervals[i][0]) {
            result.push_back(intervals[i]);
            i++;
        }

        if (result.empty() || result.back()[1] < newStart) {
            result.push_back(newInterval);
        } else {
            result.back()[1] = max(result.back()[1], newEnd);
        }

        while (i < n) {
            int start = intervals[i][0];
            int end = intervals[i][1];

            if (result.back()[1] < start) {
                result.push_back(intervals[i]);
            } else {
                result.back()[1] = max(result.back()[1], end);
            }
            i++;
        }

        return result;
    }
};
