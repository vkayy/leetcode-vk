from typing import List

class Solution:
  def largestPerimeter(self, nums: List[int]) -> int:
    nums.sort()
    total = sum(nums)
    for i in range(len(nums)-1, 1, -1):
      total -= nums[i]
      if nums[i] < total:
        return total + nums[i]
    return -1

# first, sort
# then, find the highest perimeter
# if the highest perimeter is valid, return it
# if not, try the next highest perimeter
# if no valid perimeter is found, return -1
