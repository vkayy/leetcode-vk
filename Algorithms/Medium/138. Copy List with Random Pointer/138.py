from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToNew = { None : None }
        curr = head
        while curr:
            oldToNew[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            oldToNew[curr].next = oldToNew[curr.next]
            oldToNew[curr].random = oldToNew[curr.random]
            curr = curr.next
        return oldToNew[head]

# set up a dictionary that maps old nodes to new nodes
# set the value of None to None
# this handles the case when curr.next or curr.random is None

# first, we clone the nodes and map old nodes to new nodes
# set curr to head
# while curr is not None
# map curr to a new node with value curr.val
# set curr to curr.next

# second, we set the next and random pointers of the new nodes
# set curr to head
# while curr is not None
# set the next pointer of the new node to the new node mapped to curr.next
# set the random pointer of the new node to the new node mapped to curr.random
# set curr to curr.next
# if curr.next or curr.random is None, the value of the new node will be None
# this is handled by the dictionary mapping None to None

# return the new head