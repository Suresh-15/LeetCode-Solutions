class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

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


        """
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
        """

        
