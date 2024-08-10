class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        int start = newInterval[0], end = newInterval[1];
        int i = 0, n = intervals.length, f = -1;
        while (i < n && start > intervals[i][1]) {
            f = i;
            i++;
        }
        while (i < n && intervals[i][0] <= end) {
            start = Math.min(start, intervals[i][0]);
            end = Math.max(end, intervals[i][1]);
            i++;
        }
        int[][] result = new int[f + 2 + n - i][2];
        int ci = 0;
        while (ci <= f) {
            result[ci] = intervals[ci];
            ci++;
        }
        result[ci++] = new int[] { start, end };
        while (i < n) {
            result[ci] = intervals[i];
            ci++;
            i++;
        }
        return result;
    }
}
