class Solution:
    def myAtoi(self, s: str) -> int:
        # s = s.strip()
        result = ""
        if len(s) <= 1 and not(s.isnumeric()):
            return 0
        for i in s:
            if i == " " and len(result) == 0:
                continue
            elif (i == '+' or i == '-') and len(result) == 0:
                result += i
            else:
                if i.isnumeric():
                    result += i
                else:
                    break

        if len(result) == 0 or result == '+' or result == '-' or result=="":
            return 0
        if int(result) < pow(-2, 31):
            return pow(-2, 31)
        elif int(result) > pow(2, 31) - 1:
            return pow(2, 31) - 1
        else:
            return int(result)
            
