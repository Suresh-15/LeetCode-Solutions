class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ''
        for i in range(min([len(word1), len(word2)])):
            s = s + word1[i]
            s = s + word2[i]
        if(len(word1) < len(word2)):
            s = s + word2[len(word1):]
        else:
            s = s + word1[len(word2):]
        return s 