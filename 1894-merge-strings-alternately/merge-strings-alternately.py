class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ''
        sizes = [len(word1), len(word2)]
        for i in range(min(sizes)):
            s = s + word1[i]
            s = s + word2[i]
        if(sizes[0] < sizes[1]):
            s = s + word2[sizes[0]:]
        else:
            s = s + word1[sizes[1]:]
        return s 