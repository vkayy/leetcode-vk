from typing import List
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(child) for child in root.children) if root.children else 1

# first, check if the root is None
# if so, return 0

# return 1 plus the maximum of the maximum depth of each child of the root if the root has children, otherwise 1