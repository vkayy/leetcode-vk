from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
  def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(None, head)
    prev, curr = dummy, head
    while curr and curr.next:
      prev.next = curr.next
      curr.next = curr.next.next
      prev.next.next = curr
      prev, curr = curr, curr.next
    return dummy.next

# first, we create a dummy node with the value None and the next node as the head
# then we create two pointers, prev and curr, and initialise them with the dummy node and the head

# then we iterate through the list
# if the current node and the next node exist
# the previous node's next node becomes the next node
# the current node's next node becomes the next node's next node
# the next node's next node becomes the current node
# then we move the previous and current nodes to the next pair of nodes
