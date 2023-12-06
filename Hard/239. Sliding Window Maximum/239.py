from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        dq = deque()
        
        l, r = 0, 0
        
        while r < len(nums):
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()
            dq.append(r)
            
            if l > dq[0]:
                dq.popleft()
            
            if (r - l + 1 >= k):
                res.append(nums[dq[0]])
                l += 1
            r += 1
        
        return res

# initialise the result and a deque

# initialise the left and right pointers to 0

# while the right pointer is less than the length of the array

# while the deque is non-empty and the last element of the deque is less than the current element
# this means that the last element of the deque is not the maximum element
# so, we can remove it, as we are only concerned with the maximum

# then, we can add the current element to the deque

# if the left pointer is greater than the first element of the deque
# i.e., the first element of the deque is out of bounds
# then, we can remove it

# if the window size is greater than or equal to k
# then, we can add the first element of the deque to the result
# this is because the first element of the deque is the maximum element in the window
# then, we can increment the left pointer

# then, we can increment the right pointer