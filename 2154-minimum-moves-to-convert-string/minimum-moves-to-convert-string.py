class Solution:
    def minimumMoves(self, s: str) -> int:
        moves = 0
        for i in range(len(s) - 3 + 1):
            if s[i] == 'X':
                s = s[:i] + 'OOO' + s[i + 3:]
                moves += 1

        else:
            if 'X' in s[len(s) - 3: len(s)]:
                s = s[:len(s) - 3] + 'OOO'
                moves += 1
         
        return moves