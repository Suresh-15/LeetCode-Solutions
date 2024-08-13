class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dictionary = {}
        words = s.split(" ")
        if len(pattern) != len(words):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in dictionary.keys() and words[i] in dictionary.values():
                return False
            elif pattern[i] in dictionary.keys() and dictionary[pattern[i]] != words[i]:
                return False
            elif pattern[i] not in dictionary.keys():
                dictionary[pattern[i]] = words[i]

        return True
