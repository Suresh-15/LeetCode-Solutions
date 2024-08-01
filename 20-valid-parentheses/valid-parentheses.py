class Solution:
    def isValid(self, s: str) -> bool:
        opens = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                opens.append(i)
            elif len(opens) != 0:
                character = opens.pop()
                if i == ')':
                    if character != '(':
                        return False
                elif  i == '}':
                    if character != '{':
                        return False
                elif  i == ']':
                    if character != '[':
                        return False
            else:
                return False
                
        if len(opens) != 0:
            return False
        return True

