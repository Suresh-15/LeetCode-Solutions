class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        pq = [-i for i in nums]
        heapify(pq)
        score = 0
        for _ in range(k):
            score -= pq[0]
            heapreplace(pq, pq[0] // 3)
        return score
