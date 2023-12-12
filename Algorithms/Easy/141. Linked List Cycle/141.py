from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

# set slow and fast pointer to the head
# while fast exists and fast.next exists
# set slow to the next item
# set fast to the next next item
# if slow is fast, i.e., a cycle found, return true
# if no cycle is found, return false