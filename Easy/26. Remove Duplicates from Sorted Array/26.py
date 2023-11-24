from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 0
        N = len(nums)
        for i in range(N - 1):
            if nums[i] != nums[i + 1]:
                nums[j] = nums[i]
                j += 1
        nums[j] = nums[N - 1]
        return j + 1

# initiate current index pointer and new index pointer
# set N to list length
# iterate through the first N - 1 elements
# if the number is different to the proceeding number
# set nums[j] to that number, and increment j
# j points to the new index
# then, after this, we will have not checked the last element
# either it is the same as the 2nd last element or different
# if it is the same, it is assigned to the last element
# if it is different, the 2nd last element has already been added
# so, we assign the last element to the j pointer regardless