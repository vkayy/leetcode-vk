from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
  def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    curr = dummy
    while curr:
      while curr.next and curr.next.val == val:
        curr.next = curr.next.next
      curr = curr.next
    return dummy.next

# first, we create a dummy node with the value 0 and the next node as the head
# then we create a pointer, curr, and initialise it with the dummy node
# while the current node exists
# if the current node's next node exists and has the value we want to remove
# the current node's next node becomes the next node's next node
# then we move the current node to the next node
# finally, we return the dummy node's next node
# this is because the dummy node is a placeholder and the next node is the actual head of the list
# therefore, we return the next node
