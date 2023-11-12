from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        N, tail = 1, head
        while tail.next:
            tail = tail.next
            N += 1
        tail.next = head

        k %= N
        k = N - k

        new_tail, new_head = head, head
        for _ in range(k - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None

        return new_head

# if the list is empty or has one element or is rotated by 0 places,
# return the list
# otherwise, get no. of nodes N in list while creating a cycle
# apply modulus of N to k (same effect as rotating by k places)
# k is k subtract N
# new tail is k - 1 nodes away from head
# new head is after new tail
# new tail has no next; cuts cycle
# return new head