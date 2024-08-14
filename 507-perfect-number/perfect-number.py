class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False

        answer, i = 1, 2
        while i * i < num:
            if num % i == 0:
                answer += i + num // i
            i += 1
        if i * i == num:
            answer += i

        return answer == num
