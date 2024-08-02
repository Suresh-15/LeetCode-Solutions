# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        # return result
        # return  [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)  if root else []
"""
    def preorder(root, result: List[int]):
            if root is None:
                return
            result.append(root.val)
            preorder(root.left)
            preorder(root.right)
"""    