from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev, curr = None, head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

# if the list is empty or singular, return it as it is symmetric
# set prev to none, and curr to the head
# while curr is not null
# temp hold the node after curr in next
# set the node after curr to prev
# set prev to curr, swapping the two
# move curr to the next node
# effectively swaps across