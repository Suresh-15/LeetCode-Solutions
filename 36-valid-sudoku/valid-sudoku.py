class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cube = defaultdict(set)
        rows = defaultdict(set)
        cols = defaultdict(set)

        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element.isalnum():
                    k = i // 3 * 3 + j // 3
                    if element in rows[i] or element in cols[j] or element in cube[k]:
                        return False
                    else:
                        rows[i].add(element)
                        cols[j].add(element)
                        cube[k].add(element)

        return True
