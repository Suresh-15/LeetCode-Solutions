class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # nums.sort(reverse = True, key= lambda x: nums.count(x))
        """
        dictionary = { num: nums.count(num) for num in nums }
        output = []
        for i in dictionary:
            if dictionary[i] >= k:
                output.append(i)
        output.sort(reverse = True, key = lambda x: nums.count(x))
        if output == []:
            return nums
        return output


        freq_map = {}
        buckets = [[] for _ in range(len(nums) + 1)]
        top_k = []
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        for num, freq in freq_map.items():
            buckets[freq].append(num)
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                top_k.append(num)
                if len(top_k) == k:
                    return top_k
        

        from collections import defaultdict
        d = defaultdict(int)
        for num in nums:
            d[num] += 1

        heap = []
        for (key, v) in d.items():
            heappush(heap, (v,key))
            if len(heap) > k:
                heappop(heap)

        return [k for (v, k) in heap]

        """

        defDict = defaultdict(int)
        for number in nums:
            defDict[number] += 1
        return sorted(defDict, key=defDict.get, reverse=True)[:k]