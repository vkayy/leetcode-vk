from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, idx = 0, 0
        while i < len(nums):
            if nums[i] != 0:
                nums[idx], nums[i] = nums[i], nums[idx]
                idx += 1
            i += 1

# we can use two pointers to keep track of the index of the next non-zero element
# we can iterate through the array
# if the current element is not zero, we can swap it with the element at the next non-zero index
# then, we can increment the next non-zero index
# then, we can increment the iterator