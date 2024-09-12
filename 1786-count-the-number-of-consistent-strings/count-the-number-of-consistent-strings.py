class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        characters = set(allowed)
        for word in words:
            for char in set(word):
                if char not in characters:
                    count += 1
                    break
        
        return len(words) - count