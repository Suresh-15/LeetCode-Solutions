class Solution:
    def maxPathLength(self, coordinates: List[List[int]], k: int) -> int:
        def maxEnvelopes(envelopes: list[list[int]]) -> int:
            envelopes.sort(key=lambda x: (x[0], -x[1]))  
            lis = []
            for i, (width, height) in enumerate(envelopes):
                pos = bisect_left(lis, height)
                if pos == len(lis):  
                    lis.append(height)
                else:
                    lis[pos] = height

            return len(lis)

        mi, mj = coordinates[k]
        group1 = [[i,j] for i,j in coordinates if i < mi and j < mj]
        group2 = [[i,j] for i,j in coordinates if i > mi and j > mj]

        return maxEnvelopes(group1) + maxEnvelopes(group2) + 1