class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        if len(intervals) <= 1:
            return intervals

        intervals.sort(key=lambda x: x[0])
        print(intervals)
        start, end = intervals[0][0], intervals[0][1]
        for i in range(1, len(intervals)):
            if end >= intervals[i][0]:
                end = max(end, intervals[i][1])
            else:
                result.append([start, end])
                start, end = intervals[i][0], intervals[i][1]
        else:
            result.append([start, end])
        
        return result
