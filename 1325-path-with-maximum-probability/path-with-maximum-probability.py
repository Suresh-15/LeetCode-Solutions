class Solution:
    def maxProbability(
        self, n: int, edges: List[List[int]],
        succProb: List[float], start_node: int, end_node: int,
    ) -> float:

        graph = defaultdict(list)
        for i in range(len(edges)):
            a, b = edges[i]
            prob = succProb[i]
            graph[a].append((b, prob))
            graph[b].append((a, prob))

        max_heap = [(-1, start_node)]
        max_prob = [0.0] * n
        max_prob[start_node] = 1.0

        while max_heap:
            curr_prob, node = heapq.heappop(max_heap)
            curr_prob = -curr_prob  
            if node == end_node:
                return curr_prob

            for neighbor, edge_prob in graph[node]:
                new_prob = curr_prob * edge_prob
                if new_prob > max_prob[neighbor]:
                    max_prob[neighbor] = new_prob
                    heapq.heappush(max_heap, (-new_prob, neighbor))

        return 0.0
