class Solution:
    def maxValue(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def get_possible(a):
            t1 = {(0, 0)}
            d = defaultdict(lambda: -1)
            for i, x in enumerate(a):
                t2 = set()
                for taken, val in t1:
                    if taken < k:
                        t2.add((taken + 1, val | x))
                        if taken + 1 == k and val | x not in d:
                            d[val | x] = i + 1
                t1.update(t2)
            return d

        a = get_possible(nums)
        b = get_possible(nums[::-1])
        ans = -float("inf")

        for v1, x in a.items():
            for v2, y in b.items():
                if x + y <= n:
                    ans = max(ans, v1 ^ v2)

        return ans
