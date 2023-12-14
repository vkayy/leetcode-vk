from typing import List
from collections import deque

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        q, res = deque([root]), []
        while q:
            sub = []
            for _ in range(len(q)):
                curr = q.popleft()
                sub.append(curr.val)
                q.extend(curr.children)
            res.append(sub)
        return res

# breadth-first search level order traversal