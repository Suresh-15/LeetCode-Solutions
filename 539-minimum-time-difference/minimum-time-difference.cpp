class Solution {
public:
    int findMinDifference(vector<string>& timePoints) {
        vector<int> minutes(timePoints.size());
        for (int i = 0; i < timePoints.size(); i++) {
            int hour = stoi(timePoints[i].substr(0, 2));
            int mins = stoi(timePoints[i].substr(3, 5));
            minutes[i] = hour * 60 + mins;
        }

        sort(minutes.begin(), minutes.end());
        int m = 1440 - minutes.back() + minutes.front();
        for (int i = 0; i < minutes.size() - 1; i++)
            m = min(m, minutes[i + 1] - minutes[i]);

        return m;        
    }
};