class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words = defaultdict(lambda: 0)
        for word in list(s1.split()):
            words[word] += 1
        for word in list(s2.split()):
            words[word] += 1

        result = []
        for key, value in words.items():
            if value == 1:
                result.append(key)

        return result