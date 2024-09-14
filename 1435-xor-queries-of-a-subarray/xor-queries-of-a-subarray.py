class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        output = []
        prefix_xors = [0]
        for i in range(len(arr)):
            prefix_xors.append(prefix_xors[i] ^ arr[i])
        for q in queries:
            output.append(prefix_xors[q[0]] ^ prefix_xors[q[1] + 1])
        return output
        
            
