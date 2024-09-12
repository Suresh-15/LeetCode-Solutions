class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        result = 0

        for word in words:
            characters = set(list(word))
            for i in characters:
                if i not in allowed:
                    break
            else:
                result += 1
        
        else:
            return result