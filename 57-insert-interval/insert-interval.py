class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        ans = [intervals[0]]
        for i in range(1, len(intervals)):
            a = ans[-1]
            b = intervals[i]
            if a[1] >= b[0]:
                ans[-1][1] = max(a[1], b[1])
            else:
                ans.append(b)
        return ans