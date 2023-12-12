from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr1, curr2 = list1, list2
        dummy = ListNode(-1)
        tail = dummy
        
        while curr1 and curr2:
            if curr1.val < curr2.val:
                tail.next = curr1
                curr1 = curr1.next
            else:
                tail.next = curr2
                curr2 = curr2.next
            tail = tail.next
        
        if curr1:
            tail.next = curr1
        elif curr2:
            tail.next = curr2
                
        return dummy.next

# first, set the current node of the first list to the head of the first list
# set the current node of the second list to the head of the second list
# set the dummy node to a new node with a value of -1
# set the tail node to the dummy node

# while the current node of the first list and the current node of the second list are not None

# if the value of the current node of the first list is less than the value of the current node of the second list
# set the next node of the tail node to the current node of the first list
# set the current node of the first list to the next node of the current node of the first list

# otherwise, the value of the current node of the second list is less than or equal to the value of the current node of the first list
# set the next node of the tail node to the current node of the second list
# set the current node of the second list to the next node of the current node of the second list

# set the tail node to the next node of the tail node

# if the current node of the first list is not None
# set the next node of the tail node to the current node of the first list

# otherwise, the current node of the second list is not None
# set the next node of the tail node to the current node of the second list

# return the next node of the dummy node