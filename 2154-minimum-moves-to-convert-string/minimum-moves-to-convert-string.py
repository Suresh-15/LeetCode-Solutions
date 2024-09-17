class Solution:
    def minimumMoves(self, string: str) -> int:
        moves: int = 0
        if string:
            idx, size = 0, len(string)
            while idx < size:
                if string[idx] == 'X':
                    moves += 1
                    idx += 3
                else:
                    idx += 1
        
        return moves