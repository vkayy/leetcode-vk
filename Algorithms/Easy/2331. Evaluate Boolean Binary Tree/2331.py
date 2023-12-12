from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return root.val
        if root.val == 2:  
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)
        return self.evaluateTree(root.left) and self.evaluateTree(root.right)

# if the root is a leaf node, we can return the value of the leaf node
# if the root is an OR node, we can return the OR of the left and right subtrees
# if the root is an AND node, we can return the AND of the left and right subtrees