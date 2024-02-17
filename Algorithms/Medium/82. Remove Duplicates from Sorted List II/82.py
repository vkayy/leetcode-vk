from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
  def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    prev, curr = dummy, head
    while curr:
      while curr.next and curr.val == curr.next.val: 
        curr = curr.next
      if prev.next == curr:
        prev = curr
      else:
        prev.next = curr.next
      curr = curr.next
    return dummy.next

# the idea is to use a dummy node to handle the edge case of the head node being a duplicate
# we use two pointers to iterate through the linked list
# we use a while loop to iterate through the linked list
# we use another while loop to skip over the duplicates
# if the previous node's next is the current node, we update the previous node
# otherwise, we update the previous node's next to the current node's next
# we update the current node to the next node
# finally, we return the dummy node's next node

