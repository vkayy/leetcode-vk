from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        tmp = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(tmp)
        
        return root

# first, check if the root is None
# if so, return None

# set the temporary node to the left node of the root
# set the left node of the root to the inverted right node of the root
# set the right node of the root to the inverted temporary node

# return the root