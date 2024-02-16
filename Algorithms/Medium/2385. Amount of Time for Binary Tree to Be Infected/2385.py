from typing import Optional
from collections import deque, defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
  def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
    def dfs(root):
      nonlocal adj
      if not root:
        return
      if root.left:
        adj[root.val].append(root.left.val)
        adj[root.left.val].append(root.val)
      if root.right:
        adj[root.val].append(root.right.val)
        adj[root.right.val].append(root.val)
      dfs(root.left)
      dfs(root.right)
    adj = defaultdict(list)
    dfs(root)
    q, v = deque([start]), set([start])
    time = -1
    while q:
      time += 1
      for _ in range(len(q)):
        curr = q.popleft()
        v.add(curr)
        for n in adj[curr]:
          if n not in v:
            q.append(n)
    return time

# first, we create an adjacency list for the binary tree
# then we use breadth-first search to find the amount of time for the binary tree to be infected
# we initialise a queue with the start node
# we initialise a set with the start node for visited nodes
# we initialise the time as -1
# we then perform breadth-first search
# the bfs is modified to count the number of levels
# this is done by having a for loop to iterate through the nodes at each level
