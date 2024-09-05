class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total_elements = len(rolls) + n
        sum_of_all_elements = total_elements * mean
        sum_of_second_list = sum_of_all_elements - sum(rolls)
        if sum_of_second_list > 6 * n or sum_of_second_list < n:
            return []

        second_list = [1] * n
        missing_sum = sum_of_second_list - n

        for i in range(n):
            
            second_list[i] += min(5, missing_sum)
            missing_sum -= 5
            
            if missing_sum <= 0:
                break

        return second_list
