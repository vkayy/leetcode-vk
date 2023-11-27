from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inRange(root, l, r) -> bool:
            if not root:
                return True
            return l < root.val and root.val < r and inRange(root.left, l, root.val) and inRange(root.right, root.val, r)
        
        return inRange(root, float("-inf"), float("inf"))

# first, define a function that checks if the value of the root is in the range of l and r
# if the root is None, return True
# if the value of the root is not in the range of l and r, return False
# return the result of checking if the value of the root is in the range of l and r
# and recursively checking if the left node of the root is in the range of l and the value of the root
# and recursively checking if the right node of the root is in the range of the value of the root and r

# return the result of checking if the root is in the range of negative infinity and positive infinity