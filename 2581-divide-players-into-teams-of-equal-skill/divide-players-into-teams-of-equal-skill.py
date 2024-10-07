class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        pairSum = sum(skill) // (n // 2)
        answer = 0
        count = Counter(skill)

        for key, value in count.items():
            other = pairSum - key
            if count[other] != value:
                return -1
            answer += key * other * value

        return answer // 2
