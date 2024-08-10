class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        int newStart = newInterval[0];
        int newEnd = newInterval[1];
        int i = 0, n = intervals.length;
        List<int[]> result = new ArrayList<>();

        while (i < n && newStart > intervals[i][0]) {
            result.add(intervals[i]);
            i++;
        }

        if (result.isEmpty() || result.get(result.size() - 1)[1] < newStart) {
            result.add(newInterval);
        } else {
            result.get(result.size() - 1)[1] = Math.max(result.get(result.size() - 1)[1], newEnd);
        }
        while (i < n) {
            int start = intervals[i][0];
            int end = intervals[i][1];

            if (result.get(result.size() - 1)[1] < start) {
                result.add(intervals[i]);
            } else {
                result.get(result.size() - 1)[1] = Math.max(result.get(result.size() - 1)[1], end);
            }
            i++;
        }
        return result.toArray(new int[result.size()][]);
    }
}
