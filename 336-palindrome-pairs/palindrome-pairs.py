class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        """
        answers = list()
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                s1 = words[i] + words[j]
                s2 = words[j] + words[i]
                if s1 == s1[::-1]:
                    answers.append([i, j])
                if s2 == s2[::-1]:
                    answers.append([j, i])
        return answers

        word_dict = { word: index for index, word in enumerate(words) }
        result = []

        for index, word in enumerate(words):
            for j in range(len(word) + 1):
                left = word[:j]
                reversed_left = left[::-1]
                right = word[j:]
                reversed_right = right[::-1]

                if reversed_left in word_dict \
                    and word_dict[reversed_left] != index \
                    and right == reversed_right:
                    result.append([index, word_dict[reversed_left]])
                
                if j > 0 \
                    and reversed_right in word_dict \
                    and word_dict[reversed_right] != index \
                    and left == reversed_left:
                    result.append([word_dict[reversed_right], index])
            
        return result
        """

        res = []
        words = sorted(chain(
            ((i, w, False) for i, w in enumerate(words)), 
            ((i, w[::-1], True) for i, w in enumerate(words))),
            key=lambda x: x[1])
        
        for i, (idx1, w1, is_reversed1) in enumerate(words):
            for j in range(i + 1, len(words)):
                idx2, w2, is_reversed2 = words[j]
                if w2.startswith(w1):
                    if is_reversed1 == is_reversed2:
                        continue
                    rest = w2[len(w1):]
                    if idx1 != idx2 and rest == rest[::-1]:
                        res += [(idx1, idx2) if is_reversed2 else (idx2, idx1)]
                else:
                    break
        return res