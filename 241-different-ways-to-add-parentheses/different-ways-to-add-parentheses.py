class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        result = []
        for i in range(len(expression)):
            oper = expression[i]
            if oper == "+" or oper == "-" or oper == "*":
                sub_str1 = expression[0 : i]
                sub_str2 = expression[i + 1 : ]
                s1 = self.diffWaysToCompute(sub_str1)
                s2 = self.diffWaysToCompute(sub_str2)
                for i in s1:
                    for j in s2:
                        if oper == "*":
                            result.append(int(i) * int(j))
                        if oper == "+":
                            result.append(int(i) + int(j))
                        if oper == "-":
                            result.append(int(i) - int(j))
        if len(result) == 0:
            result.append(int(expression))
        return result