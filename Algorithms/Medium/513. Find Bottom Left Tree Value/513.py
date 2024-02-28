from typing import Optional
from collections import deque

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
    q = deque([root])
    while q:
      curr = q.popleft()
      if curr.right:
        q.append(curr.right)
      if curr.left:
        q.append(curr.left)
    return curr.val

# we perform a breadth-first search on the tree
# we add the right child first, then the left child
# we return the value of the last node we visit
# this works because we add the right child first, then the left child
# therefore, the last node we visit will be the leftmost node in the last row
