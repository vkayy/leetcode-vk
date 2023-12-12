class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "None"
        
        return ",".join([str(root.val), self.serialize(root.left), self.serialize(root.right)])
    

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        def dfs(nodes):
            nonlocal i
            if nodes[i] == "None":
                i += 1
                return None
            node = TreeNode(int(nodes[i]))
            i += 1
            node.left = dfs(nodes)
            node.right = dfs(nodes)
            return node
        
        i = 0
        return dfs(data.split(","))
        
                
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

# serialize is just a preorder traversal
# deserialize converts a preorder traversal to a tree

# in deserialize, we define a function that performs a depth-first search
# we set i to nonlocal because we want to be able to update the index

# if the current node is None
# return None

# if the current node is not "None"
# create a node with the value of the current node
# increment i by 1
# recursively call the function with the nodes for the left
# recursively call the function with the nodes for the right
# this works because i is incremented by 1 each time a node is created