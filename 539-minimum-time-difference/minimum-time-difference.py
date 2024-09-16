class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def getMinutes(s):
            time = s.split(":")
            return int(time[0]) * 60 + int(time[1])

        times, points = set(), []
        for i in timePoints:
            s = getMinutes(i)
            if s in times:
                return 0
            times.add(s)
            points.append(s)

        points.sort()
        m = 24 * 60 - points[-1] + points[0]
        for i in range(len(points) - 1):
            m = min(m, points[i + 1] - points[i])
        return m
