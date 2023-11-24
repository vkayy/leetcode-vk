from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if not fast or not fast.next:
            return
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow

# set slow and fast pointer to the head
# while fast and fast.next exist
# set slow to slow.next, fast to fast.next.next
# if slow and fast are equal exit loop
# if the loop exited because we reached a null
# return null
# if not, set slow to head
# while slow isnt equal to fast
# set them to traverse at the same rate
# they will meet where the cycle starts
# return slow once they meet as this is where the cycle starts