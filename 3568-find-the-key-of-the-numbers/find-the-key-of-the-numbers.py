class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        n1, n2, n3 = str(num1), str(num2), str(num3)
        while len(n1) < 4:
            n1 = '0' + n1
        while len(n2) < 4:
            n2 = '0' + n2
        while len(n3) < 4:
            n3 = '0' + n3
        
        result = ''
        for i in range(4):
            result += str(min(int(n1[i]), int(n2[i]), int(n3[i])))
        return int(result)