from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            if target > nums[mid]:
                low = mid + 1
            
            elif target < nums[mid]:
                high = mid - 1
            
            else:
                return mid
        
        return -1

# first, set the low pointer to zero and the high pointer to the last index
# iterate while the low pointer is less than or equal to the high pointer
# set the mid pointer to the average of the low and high pointers
# if the target is greater than the number at the mid pointer
# set the low pointer to the mid pointer plus one
# if the target is less than the number at the mid pointer
# set the high pointer to the mid pointer minus one
# else, return the mid pointer
# return -1 if no element found