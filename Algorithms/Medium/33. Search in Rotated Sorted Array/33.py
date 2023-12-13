from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2
            
            if target == nums[m]:
                return m
            
            if nums[m] >= nums[l]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
            
        return -1

# first, set the left pointer to zero and the right pointer to the last index
# iterate while the left pointer is less than or equal to the right pointer

# set the mid pointer to the average of the left and right pointers

# if the target is equal to the number at the mid pointer
# return the mid pointer

# if the number at the mid pointer is greater than or equal to the number at the left pointer
# the mid pointer is in the left sorted array which is greater than the right sorted array

# if the target is greater than the number at the mid pointer or the target is less than the number at the left pointer
# the target is not in the left sorted array
# set the left pointer to the mid pointer plus one to search the right sorted array

# otherwise, the target is in the left sorted array
# set the right pointer to the mid pointer minus one to search the left sorted array

# otherwise, the number at the mid pointer is less than the number at the left pointer
# the mid pointer is in the right sorted array which is less than the left sorted array

# if the target is less than the number at the mid pointer or the target is greater than the number at the right pointer
# the target is not in the right sorted array
# set the right pointer to the mid pointer minus one to search the left sorted array

# otherwise, the target is in the right sorted array
# set the left pointer to the mid pointer plus one to search the right sorted array

# return -1 if no element found

