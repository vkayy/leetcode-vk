from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        traversal = []
        queue = deque()
        queue.append(root)
        
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level:
                traversal.append(level)
        return traversal

# first, define a list to store the traversal
# then, define a queue to store the nodes
# append the root to the queue

# while the queue is not empty
# define a list to store the current level

# for each node in the queue
# pop the leftmost node from the queue

# if the node exists
# append the value of the node to the current level
# append the left node of the node to the queue
# append the right node of the node to the queue

# if the current level is not empty
# append the current level to the traversal

# return the traversal