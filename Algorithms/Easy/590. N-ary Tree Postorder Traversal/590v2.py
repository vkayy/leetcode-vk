from typing import List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stk, res = [root], []
        while stk:
            curr = stk.pop()
            res.append(curr.val)
            stk.extend(curr.children or [])
        return res[::-1]

# iterative solution