class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        if start == goal:
            return 0

        sbin = str(bin(start))[2:]
        ebin = str(bin(goal))[2:]

        s, e = len(sbin), len(ebin)
        difference = abs(s - e)
        if s < e:
            sbin = '0' * difference + sbin
        else:
            ebin = '0' * difference + ebin 

        count = 0
        for i in range(len(sbin)):
            if sbin[i] != ebin[i]:
                count += 1
        return count