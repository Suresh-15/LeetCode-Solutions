class Solution:
    def partitionString(self, s: str) -> int:
        temp, result = '', []

        for i in s:
            if i not in temp:
                temp += i
            else:
                result.append(temp)
                temp = i
        else:
            result.append(temp)

        print(result)
        return len(result)