from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return
        if len(nums) == 1:
            return TreeNode(nums[0])
        m = len(nums) // 2
        root = TreeNode(nums[m])
        root.left = self.sortedArrayToBST(nums[:m])
        root.right = self.sortedArrayToBST(nums[m + 1:])
        return root

# first, check if the list is empty
# if it is, then return None

# then, check if the list has only one element
# if it does, then return a new node with the value of the element

# otherwise, find the middle index of the list
# then, create a new node with the value of the middle element
# then, recursively call the function on the left and right halves of the list
# then, set the left and right children of the new node to the results of the recursive calls
# finally, return the new node