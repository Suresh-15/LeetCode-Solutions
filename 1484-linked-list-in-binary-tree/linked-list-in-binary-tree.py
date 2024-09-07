# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def check_next_node(self, head, root):
        checkLeft, checkRight = False, False
        if not head:
            return True
        if root.left and root.left.val == head.val:
            checkLeft = self.check_next_node(head.next, root.left)
        if root.right and root.right.val == head.val:
            checkRight = self.check_next_node(head.next, root.right)

        return checkLeft or checkRight

    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if root.val == head.val:
            if self.check_next_node(head.next, root):
                return True

        checkLeft = self.isSubPath(head, root.left)
        checkRight = self.isSubPath(head, root.right)

        return checkLeft or checkRight
