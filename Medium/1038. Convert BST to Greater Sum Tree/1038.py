from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        total = 0
        def convert(node):
            nonlocal total
            if not node:
                return None
            convert(node.right)
            total += node.val
            node.val = total
            convert(node.left)
        convert(root)
        return root

# for each node, we want to add the sum of all nodes greater than it to it
# we can do this by traversing the tree in reverse inorder
# this way, we will visit the nodes in descending order
# we can keep track of the total sum in a variable
# we can then add the current node's value to the total sum
# then, we can set the current node's value to the total sum
# then, we can traverse the left subtree
# then, we can return the root