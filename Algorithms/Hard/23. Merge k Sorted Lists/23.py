from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        def mergeList(l1, l2):
            dummy = ListNode(-1)
            tail = dummy
            while l1 and l2:
                if l1.val >= l2.val:
                    tail.next = l2
                    l2 = l2.next
                else:
                    tail.next = l1
                    l1 = l1.next
                tail = tail.next
            if l1:
                tail.next = l1
            else:
                tail.next = l2
            return dummy.next
        
        while len(lists) > 1:
            mergedLists = []
            
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(mergeList(l1, l2))
            lists = mergedLists
        
        return lists[0]

# first, check if the list of lists is empty
# if so, return None

# define a function to merge two lists
# this is covered in leetcode 21

# while the length of the list of lists is greater than one
# create a new list of lists to store the merged lists

# iterate over the list of lists with a step size of two
# set the first list to the current list
# set the second list to the next list if the next list exists, otherwise None
# append the merged list of the first list and the second list to the new list of lists

# set the list of lists to the new list of lists