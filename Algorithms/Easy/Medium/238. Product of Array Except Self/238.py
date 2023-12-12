from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = [1] * N
        pre, post = 1, 1
        
        for i in range(len(nums)):
            res[i] *= pre
            pre *= nums[i]
        
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= post
            post *= nums[i]
        
        return res

# create a result array of 1s
# create a pre and post variable of 1
# go through the array and multiply each element by pre
# then, multiply pre by the element
# go through the array backwards and multiply each element by post
# then, multiply post by the element
# return the result array

# this algorithm performs two passes through the array
# the first pass calculates the product of all elements before the current element
# the second pass calculates the product of all elements after the current element
# the result is the product of all elements except the current element