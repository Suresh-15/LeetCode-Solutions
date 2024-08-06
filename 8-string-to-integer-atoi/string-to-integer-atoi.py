class Solution:
    def myAtoi(self, s: str) -> int:
        num = '0123456789'
        s = s.strip()
        result = ""
        for x in s:
            if x != ' ' and (x in '-+' or x in num) and len(result) == 0:
                result += x
            elif x in num:
                result += x
            else:
                break
            
        if result == '' or result in '-+':
            return 0
        else:
            sign = 1
            if result[0] in '+-':
                sign = -1 if result[0] == '-' else 1
                result = result[1:]
        
            def str_to_int(num_str):
                result = 0
                for char in num_str:
                    result = result * 10 + (ord(char) - ord('0')) 
                return result

            num_val = str_to_int(result) * sign
            
            INT_MIN, INT_MAX = -(2**31), (2**31 - 1)
            if num_val < INT_MIN:
                return INT_MIN
            elif num_val > INT_MAX:
                return INT_MAX
            else:
                return num_val