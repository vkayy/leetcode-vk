from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2
            
            if nums[m] >= nums[l]:
                if target < nums[m]:
                    if target < nums[l]:
                        l = m + 1
                    elif target > nums[l]:
                        r = m - 1
                    else:
                        return l
                elif target > nums[m]:
                    l = m + 1
                else:
                    return m
            else:
                if target < nums[m]:
                    r = m - 1
                elif target > nums[m]:
                    if target < nums[r]:
                        l = m + 1
                    elif target > nums[r]:
                        r = m - 1
                    else:
                        return r
                else:
                    return m
    
        return -1

# first, set the left pointer to zero and the right pointer to the last index
# iterate while the left pointer is less than or equal to the right pointer

# set the mid pointer to the average of the left and right pointers

# if the number at the mid pointer is greater than or equal to the number at the left pointer
# mid is in the left sorted array which is greater than the right sorted array

# if the target is less than the number at the mid pointer

# if the target is less than the number at the left pointer
# set the left pointer to the mid pointer plus one
# if the target is greater than the number at the left pointer
# set the right pointer to the mid pointer minus one
# else, return the left pointer

# if the target is greater than the number at the mid pointer
# set the left pointer to the mid pointer plus one

# else, return the mid pointer

# otherwise, the number at the mid pointer is less than the number at the left pointer

# if the target is greater than the number at the mid pointer

# if the target is less than the number at the right pointer
# set the left pointer to the mid pointer plus one

# if the target is greater than the number at the right pointer
# set the right pointer to the mid pointer minus one
# else, return the right pointer

# else, return the mid pointer

# return -1 if no element found