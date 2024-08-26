"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def traverse(node, result):
            if node:
                for child in node.children:
                    traverse(child, result)
                result.append(node.val)
        
        result = []
        traverse(root, result)
        return result