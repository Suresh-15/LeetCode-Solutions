class Solution:
    def isValid(self, s: str) -> bool:
        opens = []
        if len(s) % 2 != 0:
            return False
        for i in s:
            if i == "(" or i == "{" or i == "[":
                opens.append(i)
            else:
                if len(opens) == 0:
                    return False

                character = opens.pop()
                if (
                    (character == "{" and i != "}")
                    or (character == "[" and i != "]")
                    or (character == "(" and i != ")")
                ):
                    return False

        if len(opens) != 0:
            return False
        return True
