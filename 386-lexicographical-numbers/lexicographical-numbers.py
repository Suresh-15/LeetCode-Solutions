class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        snums = list(map(str, list(range(1, n + 1))))
        snums.sort()
        nums = list(map(int, snums))
        return nums
