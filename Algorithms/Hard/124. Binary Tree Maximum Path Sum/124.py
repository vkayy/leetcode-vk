from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            leftMax = max(dfs(root.left), 0)
            rightMax = max(dfs(root.right), 0)

            res = max(res, root.val + leftMax + rightMax)
            return root.val + max(leftMax, rightMax)
        res = root.val
        dfs(root)
        return res

# define a function that performs a depth-first search
# if the root is None, return 0

# we set res to nonlocal because we want to be able to update the result

# recursively call the function with the left node of the root
# set the left node of the root to the maximum of the left node of the root and 0
# recursively call the function with the right node of the root
# set the right node of the root to the maximum of the right node of the root and 0
# we call max with 0 because we do not want to add negative values to the sum

# set the result to the max of the result and the value of the root plus the left node of the root plus the right node of the root
# this enables us to update the result with the maximum path sum where we split the path

# otherwise, return the value of the root plus the maximum of the left node of the root and the right node of the root
# this is the maximum path sum where we do not split the path

# call the function with the root
# this updates the result

# we set res to the value of the root
# we call the dfs with the root
# this updates the result
# we return the result