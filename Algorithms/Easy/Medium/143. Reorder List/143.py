from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None
        
        prev = None
        while second:
            next = second.next
            second.next = prev
            prev = second
            second = next
        
        first, second = head, prev
        
        while second:
            next1, next2 = first.next, second.next
            first.next = second
            second.next = next1
            first, second = next1, next2

# first, set the slow pointer to the head of the list and the fast pointer to the next node of the head of the list
# iterate while the fast pointer and the next node of the fast pointer are not None
# set the slow pointer to the next node of the slow pointer
# set the fast pointer to the next node of the next node of the fast pointer

# now, the slow pointer is at the middle of the list
# set the second node to the next node of the slow pointer
# set the next node of the slow pointer to None

# set the previous node to None
# while the second node is not None
# we are reversing the second half of the list

# set the first node to the head of the list
# set the second node to the first node of the reversed second half of the list

# while the second node is not None
# set the next node of the first node to the second node
# set the next node of the second node to the next node of the first node
# set the first node to the next node of the first node
# set the second node to the next node of the second node