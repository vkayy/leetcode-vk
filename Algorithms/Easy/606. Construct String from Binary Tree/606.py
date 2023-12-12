from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        if not root.left and not root.right:
            return str(root.val)
        if not root.left:
            return f"{root.val}()({self.tree2str(root.right)})"
        if not root.right:
            return f"{root.val}({self.tree2str(root.left)})"
        return f"{root.val}({self.tree2str(root.left)})({self.tree2str(root.right)})"

# set base cases
# if root is None, return empty string
# if root has no children, return str(root.val)
# if root has no left child, return f"{root.val}()({self.tree2str(root.right)})"
# if root has no right child, return f"{root.val}({self.tree2str(root.left)})"
# these two cases are necessary because we don't want to print empty parentheses when not needed
# otherwise, return f"{root.val}({self.tree2str(root.left)})({self.tree2str(root.right)})"