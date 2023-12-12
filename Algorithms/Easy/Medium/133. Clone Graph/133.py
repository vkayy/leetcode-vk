from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        oldToNew = {}
        
        def dfsClone(node):
            
            if node in oldToNew:
                return oldToNew[node]
            
            copy = Node(node.val)
            oldToNew[node] = copy
            
            for nei in node.neighbors:
                copy.neighbors.append(dfsClone(nei))
            return copy
    
        return dfsClone(node) if node else None

# create a hash map called oldToNew

# create a function called dfsClone that takes in a node

# if the node is in oldToNew, return the node

# create a copy of the node
# add the copy to oldToNew

# for each neighbor of the node
# append the copy of the neighbor to the neighbors of the copy
# call dfsClone on the neighbor
# return the copy

# return the copy of the node if the node exists, otherwise return None