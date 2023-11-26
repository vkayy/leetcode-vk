from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# first, check if the first tree and the second tree are None
# if so, return True

# otherwise, check if the first tree or the second tree is None
# if so, return False

# check if the value of the first tree is equal to the value of the second tree
# and, recursively check if the left node of the first tree is the same as the left node of the second tree
# and, recursively check if the right node of the first tree is the same as the right node of the second tree
# if so, return True