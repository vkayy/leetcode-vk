from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
  def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    if not root:
      return []
    return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

# first, we check if the root exists
# if not, we return an empty list
# otherwise, we return the value of the root, the result of the left subtree, and the result of the right subtree
