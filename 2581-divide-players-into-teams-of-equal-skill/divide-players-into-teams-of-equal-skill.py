class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        length = len(skill)
        total_skill = sum(skill)
        frequency = [0] * 1001

        for val in skill:
            frequency[val] += 1

        if total_skill % (length // 2) != 0:
            return -1
        
        pair_sum = total_skill // (length // 2)
        totalChemistry = 0

        for val in skill:
            other = pair_sum - val
            if frequency[other] == 0:
                return -1
            totalChemistry += val * other
            frequency[other] -= 1

        return totalChemistry // 2