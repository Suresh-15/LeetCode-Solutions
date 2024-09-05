class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total_elements = len(rolls) + n
        sum_of_all_elements = total_elements * mean
        sum_of_second_list = sum_of_all_elements - sum(rolls)
        if sum_of_second_list > 6 * n or sum_of_second_list < n:
            return []

        quotient, remainder = divmod(sum_of_second_list, n)
        return [quotient + (1 if i < remainder else 0) for i in range(n)]
            