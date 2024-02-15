from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
  def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
      return
    if not head.next or not head.next.next:
      return head
    cur, odd = head, False
    lastOdd, firstEven = None, head.next
    while cur:
      nxt = cur.next
      odd = not odd
      if odd:
        lastOdd = cur
      if cur.next:
        cur.next = cur.next.next if cur.next.next else None
      cur = nxt
    lastOdd.next = firstEven
    return head

# first, check if the list is empty or has only one or two elements
# if so, return the list

# then, iterate through the list
# if the current node is odd, update the last odd node
# if the current node is even, update the first even node
# if the current node has a next node, update the next node to the node after the next node
# if the current node has no next node, set the current node to None

# finally, set the last odd node's next node to the first even node
# return the head node
