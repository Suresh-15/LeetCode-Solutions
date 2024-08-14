class Solution(object):
    def checkPerfectNumber(self, num):
        if num == 1:
            return False
        answer = 1
        for i in range(2, (int(sqrt(num)) + 1)):
            if num % i == 0:
                answer += i
                answer += num / i
        if answer == num:
            return True
        return False
        