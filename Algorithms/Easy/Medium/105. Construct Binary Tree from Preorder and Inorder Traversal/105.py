from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        
        return root
        
# first, check if the preorder list or the inorder list is empty
# if so, return None

# then, define a variable to store the root node
# then, define a variable to store the index of the root node in the inorder list

# set the left node of the root to the result of recursively calling the function
# with the preorder list from the second element to the element at the index of the root node plus one
# and the inorder list from the first element to the element at the index of the root node

# set the right node of the root to the result of recursively calling the function
# with the preorder list from the element at the index of the root node plus one to the last element
# and the inorder list from the element at the index of the root node plus one to the last element

# return the root node