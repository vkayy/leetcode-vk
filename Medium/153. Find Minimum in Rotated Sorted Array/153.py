from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] <= nums[r]:
                return nums[l]
            m = (l + r) // 2
            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m
        return nums[m]

# set l and r to be 0 and len(nums) - 1

# while l is less than or equal to r
# i.e., while there is a range to search

# if the first element is less than or equal to the last element
# i.e., if the range is sorted
# return the first element as it is the minimum

# set m to be the middle of l and r

# if the first element is less than or equal to the middle element
# i.e., if we are in the left part of the rotated array
# set l to be m + 1
# this is because the minimum is in the right half

# otherwise, we are in the right part of the rotated array
# set r to be m
# this is because the minimum is in the left half
# we don't want to set r to be m - 1 because m could be the minimum

# return nums[m]