from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return list(set(range(len(nums) + 1)).symmetric_difference(nums))[0]

# here, we use the xor operator to find the missing number
# because a ^ a = 0, so we can use the xor operator to find the missing number
# we apply xor operator to the array and the range of the array
# the result is an array with only one element, which is the missing number