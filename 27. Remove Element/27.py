from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, 0
        N = len(nums)
        for i in range(N):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j

# one pointer for tracking traversed indices
# other pointer for tracking indices to replace
# if the value is not equal to val, add it at j then increment j
# return j as it is the size of the new array