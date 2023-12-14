from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def dfs(node, mn, mx):
            if not node:
                return mx - mn
            left = dfs(node.left, mn, node.val)
            right = dfs(node.right, node.val, mx)
            return min(left, right)
        return dfs(root, float("-inf"), float("inf"))

# first, we define a helper function dfs that takes in a node, a minimum value, and a maximum value
# if the node is None, we return the difference between the maximum and minimum values
# we then recursively call dfs on the left and right children of the node
# we return the minimum of the left and right subtrees
# we call dfs on the root node, with the minimum value being negative infinity and the maximum value being positive infinity

# the reason this works is because we are guaranteed that the left subtree will be less than the root node, and the right subtree will be greater than the root node
# so, as the traversal reaches a leaf node, we can compare the difference between the maximum and minimum values seen in the traversal