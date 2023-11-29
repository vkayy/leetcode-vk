from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        tail = dummy
        
        carry = 0
        
        while l1 or l2 or carry != 0:
            
            no1 = l1.val if l1 else 0
            no2 = l2.val if l2 else 0
            
            total = no1 + no2 + carry
            carry = total // 10
            digit = total % 10
            
            tail.next = ListNode(digit)
            tail = tail.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next

# first, we create a dummy node
# this will be the head of our linked list
# we also create a tail node and set it to the dummy node

# then, we create a variable called carry and set it to 0

# while l1 or l2 or carry is not 0
# that is, while we have not reached the end of both linked lists or there is a carry

# if l1 exists, we set no1 to the value of l1
# otherwise, we set no1 to 0
# this is to handle the case where l1 is shorter than l2
# we do the same for no2

# we set total to no1 + no2 + carry
# we set carry to total // 10
# this is to get the carry
# we set digit to total % 10
# this is to get the digit

# we set the next node of tail to a new node with the digit
# we set tail to the next node

# if l1 exists, we set l1 to the next node
# otherwise, we set l1 to None
# we do the same for l2

# finally, we return the next node of the dummy node
# this is because the dummy node is the head of our linked list
# we do not want to return the dummy node