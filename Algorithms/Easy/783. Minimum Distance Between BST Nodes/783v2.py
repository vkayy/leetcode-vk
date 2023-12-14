from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        trav, mn = inorder(root), float("inf")
        for i in range(1, len(trav)):
            if (cur := trav[i] - trav[i - 1]) < mn:
                mn = cur
        return mn

# we make an inorder traversal of the tree, and store the values in a list

# we then iterate through the list, and find the minimum difference between adjacent values