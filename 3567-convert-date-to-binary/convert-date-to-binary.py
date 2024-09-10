class Solution:
    def convertDateToBinary(self, date: str) -> str:
        nums = list(date.split('-'))
        nums = [int(num) for num in nums]
        result = []
        for i in nums:
            result.append(str(bin(i))[2:])
        return '-'.join(result)