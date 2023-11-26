from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m + n - 1
        
        while m > 0 and n > 0:
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1
        
        while n > 0:
            nums1[last] = nums2[n - 1]
            n, last = n - 1, last - 1

# first, set the last index to the sum of the lengths of the two lists minus one
# iterate while the first list has elements and the second list has elements

# if the last element of the first list is greater than or equal to the last element of the second list
# set the last element of the first list to the last element of the first list
# decrement the last index

# otherwise, the last element of the second list is greater than the last element of the first list
# set the last element of the first list to the last element of the second list
# decrement the last index

# decrement the length of the first list or the second list

# iterate while the second list has elements
# set the last element of the first list to the last element of the second list
# decrement the length of the second list
# decrement the last index
