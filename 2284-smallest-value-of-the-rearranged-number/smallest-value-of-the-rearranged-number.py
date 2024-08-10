class Solution:
    def smallestNumber(self, num: int) -> int:
        sign = '+'
        if num < 0:
            sign = '-'
        
        num = abs(num)
        digits = list(str(num))
        if sign == '+':
            digits.sort(reverse=False)
            zeros = digits.count('0')
            output = ''.join(digits)
            output = int(output)
            if zeros > 0:
                output = str(output)
                output = output[0] + '0'*zeros + output[1:]
                output = int(output)
        else:
            digits.sort(reverse=True)
            output = ''.join(digits)
            output = int(output)
            output = -1 * output
        
        
        return output