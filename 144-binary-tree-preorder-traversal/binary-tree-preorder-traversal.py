# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def preorder(root):
            if root is None:
                return
            result.append(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return result


        # return  [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)  if root else []