from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        v, q = [], deque([root])
        while q:
            rmx = None
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    rmx = node.val
                    q.append(node.left)
                    q.append(node.right)
            if rmx is not None:
                v.append(rmx)
        return v

# we can use BFS to traverse the tree
# we can keep track of the rightmost node at each level
# we can add the rightmost node's value to the result
# then, we can return the result