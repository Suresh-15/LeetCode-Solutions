# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        current = head
        matrix = [[-1] * n for _ in range(m)]
        r, c, p = 0, 0, 0
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while current:
            matrix [r][c] = current.val
            current = current.next
            next_row, next_col = r + d[p % 4][0], c + d[p % 4][1]
            if 0 <= next_row < m and 0 <= next_col < n and matrix[next_row][next_col] == -1:
                r, c = next_row, next_col
            else:
                p += 1
                r, c = r + d[p % 4][0], c + d[p % 4][1]

        return matrix