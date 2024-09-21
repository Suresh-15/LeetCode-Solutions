class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        num, lexOrderList = 1, []

        for i in range(n):
            lexOrderList.append(num)
            if num * 10 <= n:
                num *= 10
            else:
                while num % 10 == 9 or num + 1 > n:
                    num //= 10
                num += 1
        return lexOrderList