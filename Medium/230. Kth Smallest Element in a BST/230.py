from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        curr = root
        
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            n += 1
            if n == k:
                return curr.val
            curr = curr.right

# first, define a variable to store the number of nodes
# then, define a stack to store the nodes
# then, define a variable to store the current node

# we perform an iterative in-order traversal

# while the current node exists or the stack is not empty
# while the current node exists

# append the current node to the stack
# set the current node to the left node of the current node

# if the current node does not exist
# pop the topmost node from the stack
# increment the number of nodes by 1

# if the number of nodes is equal to k
# return the value of the current node

# set the current node to the right node of the current node
