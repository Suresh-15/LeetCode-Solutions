class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        output = []
        prefix_xors = [0]
        for i in range(len(arr)):
            prefix_xors.append(prefix_xors[i] ^ arr[i])
        for q in queries:
            l, r = q[0], q[1]
            output.append(prefix_xors[l] ^ prefix_xors[r + 1])
        return output
        
            
