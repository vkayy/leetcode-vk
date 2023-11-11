from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy
        for _ in range(n):
            fast = fast.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next

# create a dummy list with 0
# this handles the edge cases where we remove the head of the list well
# offset slow and fast by n
# traverse slow and fast at same rate
# once fast reaches the end of the list
# slow is at the node before the one to skip
# set slow.next to the node after the next
# return dummy.next to ignore 0