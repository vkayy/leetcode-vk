from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]
        
        mn = nums[0]
        l, r = 0, len(nums) - 1
        
        while l <= r:
            if nums[l] <= nums[r]:
                mn = min(mn, nums[l])
                break
            
            m = (l + r) // 2
            mn = min(mn, nums[m])
            
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        
        return mn

# first, check if the first element is less than or equal to the last element
# if so, return the first element

# set the minimum to the first element
# set the left pointer to zero
# set the right pointer to the last index

# while the left pointer is less than the right pointer
# if number at the left pointer is less than or equal to the number at the right pointer
# set the minimum to the minimum of those two numbers
# this is because we have found the minimum element

# otherwise, set the mid pointer to the average of the left and right pointers
# set the minimum to the minimum of the number at the mid pointer and the minimum

# if the number at the mid pointer is greater than or equal to the number at the left pointer
# mid is in the left sorted array which is greater than the right sorted array
# set the left pointer to the mid pointer plus one to search the right sorted array

# otherwise, the number at the mid pointer is less than the number at the left pointer
# mid is in the right sorted array which is less than the left sorted array
# set the right pointer to the mid pointer minus one to search the left sorted array

# return the minimum