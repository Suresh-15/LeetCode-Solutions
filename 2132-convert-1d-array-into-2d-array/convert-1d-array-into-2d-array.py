class Solution:
    def construct2DArray(
        self, original: List[int], m: int, n: int
    ) -> List[List[int]]:

        if m * n != len(original):
            return []

        index, result = 0, []
        for i in range(m):
            result.append(list(original[index : index + n]))
            index += n
        return result