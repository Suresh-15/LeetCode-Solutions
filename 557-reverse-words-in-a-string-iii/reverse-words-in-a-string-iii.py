class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split(' ')
        l1 = [h[::-1] for h in l]
        result = ' '.join(l1)
        return result
        