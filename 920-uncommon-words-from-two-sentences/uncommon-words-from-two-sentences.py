class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1_n = s1.split()
        s2_n = s2.split()
        r = []

        if s1_n == s2_n:
            return r

        d1 = {}
        for i in s1_n:
            d1[i] = d1.get(i,0) +1

        d2 = {}
        for i in s2_n:
            d2[i]  = d2.get(i,0) +1


        for i in d1:
            if d1[i]==1 and (i not in d2):
                r.append(i)

        for i in d2:
            if d2[i] ==1 and (i not in d1):
                r.append(i)
        # print(r)
        return r