class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        events = []  
        for i in range(len(times)):
            events.append([times[i][0], i])  
            events.append([times[i][1], ~i])  

        events.sort() 
        available_chairs = list(
            range(len(times))
        ) 

        occupied_chairs = []
        for event in events:
            time, friend = event
            while occupied_chairs and occupied_chairs[0][0] <= time:
                _, chair = heapq.heappop(
                    occupied_chairs
                ) 
                heapq.heappush(available_chairs, chair)  # available chairs
            if friend >= 0:
                chair = heapq.heappop(available_chairs)
                if friend == targetFriend:
                    return chair
                heapq.heappush(
                    occupied_chairs, [times[friend][1], chair]
                ) 

        return -1 