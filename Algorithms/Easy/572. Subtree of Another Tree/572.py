from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    
        def isSameTree(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return t1.val == t2.val and isSameTree(t1.left, t2.left) and isSameTree(t1.right, t2.right)

        if not subRoot:
            return True
        
        if not root:
            return False
        
        return isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

# first, define a function that checks if two trees are the same
# we have covered this in leetcode 100

# then, check if the subroot is None
# if so, return True, since a None tree is a subtree of any tree

# then, check if the root is None
# if so, return False, since a None tree cannot have a non-None subtree

# return the result of checking if the root is the same as the subroot
# or, recursively checking if the left node of the root is the same as the subroot
# or, recursively checking if the right node of the root is the same as the subroot