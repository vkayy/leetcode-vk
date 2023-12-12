from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return [] if not root else self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

# set base case
# if root is None, return empty list

# otherwise, return the inorder traversal of the left subtree, the root, and the inorder traversal of the right subtree