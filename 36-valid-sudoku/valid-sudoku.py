class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            if len(set(board[i])) != 9 - board[i].count(".") + 1:
                return False

        for i in range(9):
            l = [board[x][i] for x in range(9)]
            if len(set(l)) != 9 - l.count(".") + 1:
                return False



        seen, count = set(), 0
        for i in range(0, 3):
            for j in range(0, 3):
                if board[i][j] != ".":
                    seen.add(board[i][j])
                    count += 1
        
        if len(seen) != count:
            return False

        seen, count = set(), 0
        for i in range(0, 3):
            for j in range(3, 6):
                if board[i][j] != ".":
                    seen.add(board[i][j])
                    count += 1
        
        if len(seen) != count:
            return False

        seen, count = set(), 0
        for i in range(0, 3):
            for j in range(6, 9):
                if board[i][j] != ".":
                    seen.add(board[i][j])
                    count += 1
        
        if len(seen) != count:
            return False

        seen, count = set(), 0
        for i in range(3, 6):
            for j in range(0, 3):
                if board[i][j] != ".":
                    seen.add(board[i][j])
                    count += 1
        
        if len(seen) != count:
            return False

        seen, count = set(), 0
        for i in range(3, 6):
            for j in range(3, 6):
                if board[i][j] != ".":
                    seen.add(board[i][j])
                    count += 1
        
        if len(seen) != count:
            return False

        seen, count = set(), 0
        for i in range(3, 6):
            for j in range(6, 9):
                if board[i][j] != ".":
                    seen.add(board[i][j])
                    count += 1
        
        if len(seen) != count:
            return False

        seen, count = set(), 0
        for i in range(6, 9):
            for j in range(0, 3):
                if board[i][j] != ".":
                    seen.add(board[i][j])
                    count += 1
        
        if len(seen) != count:
            return False

        seen, count = set(), 0
        for i in range(6, 9):
            for j in range(3, 6):
                if board[i][j] != ".":
                    seen.add(board[i][j])
                    count += 1
        
        if len(seen) != count:
            return False

        seen, count = set(), 0
        for i in range(6, 9):
            for j in range(6, 9):
                if board[i][j] != ".":
                    seen.add(board[i][j])
                    count += 1
        
        if len(seen) != count:
            return False


        return True