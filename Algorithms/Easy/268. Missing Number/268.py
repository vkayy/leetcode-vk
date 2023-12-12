from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(len(nums) + 1)) - sum(nums)

# we know the array contains n distinct numbers taken from 0, 1, 2, ..., n
# so we can use the sum of 0, 1, 2, ..., n to minus the sum of the array
# the result is the missing number