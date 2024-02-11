from typing import List

class Solution:
  def firstMissingPositive(self, nums: List[int]) -> int:
    for i in range(len(nums)):
      while 1 <= nums[i] <= len(nums) and nums[nums[i] - 1] != nums[i]:
        nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
    for i, n in enumerate(nums):
      if n != i + 1:
        return i + 1
    return len(nums) + 1

# here, we use the cyclic sort algorithm to sort the array
# then we iterate through the array to find the first missing positive integer
# if we don't find any missing positive integer, we return the length of the array plus 1
# this is because at this point the array must contain all positive integers from 1 to the length of the array
