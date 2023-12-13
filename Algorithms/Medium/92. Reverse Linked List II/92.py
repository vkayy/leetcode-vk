from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right or not head.next:
            return head
        
        prev, curr = None, head

        i = 1
        while i < left:
            prev = curr
            curr = curr.next
            i += 1
        
        rev_tail = curr
        rev_head = None

        while i <= right:
            next = curr.next
            curr.next = rev_head
            rev_head = curr
            curr = next
            i += 1
        
        if prev:
            prev.next = rev_head
        else:
            head = rev_head
        
        rev_tail.next = curr
        return head

# if left == right or the list has one element, no reversal occurs
# otherwise, set prev to none and curr to the head
# we will move curr to the node from which we reverse
# set i = 1 as we are at the 1st node
# while i is less than the left bound
# shift prev and curr to the next node and increment i
# once i = left, curr points at the first node to reverse
# prev also points at the node right before the reversal
# point rev_tail to curr, and point rev_head to none
# now, we reverse connections up to the right'th note
# once i > right, curr is going to point to the nodes  the reversed
# moreover, rev_head points to the front of the reversed nodes
# if prev exists, connect prev to the front of the reversed section
# otherwise, just let the head point to the front of the reversed section
# then, connect the end of the reversed section to curr, the point after