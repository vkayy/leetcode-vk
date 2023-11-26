from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return max(1 + self.maxDepth(root.left), 1 + self.maxDepth(root.right))

# first, check if the root is None
# if so, return 0

# return the maximum of 1 plus the maximum depth of the left node of the root and 1 plus the maximum depth of the right node of the root