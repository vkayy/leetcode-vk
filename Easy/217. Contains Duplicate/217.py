from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return False
        freqs = {}
        for i in range(0, len(nums)):
            if nums[i] in freqs:
                return True
            else:
                freqs[nums[i]] = 1
        return False

# go through the array and create a dictionary of frequencies
# if a number is already in the dictionary, return True
# else, add the number to the dictionary
# if the loop finishes, return False