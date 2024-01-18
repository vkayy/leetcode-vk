from typing import List

class Solution:
  def minOperations(self, nums: List[int]) -> int:
    res, N = 0, len(nums)
    while any(n != 0 for n in nums):
      for i, n in enumerate(nums):
        if n % 2:
          nums[i] -= 1
          res += 1
      if all(n == 0 for n in nums):
        break
      nums = [n / 2 for n in nums]
      res += 1
    return res

# first, we work backwards from the target array to the initial array
# first, we subtract 1 from all odd numbers
# then, we divide all numbers by 2
# we repeat this process until all numbers are 0
# we count the number of operations we perform
# we return the number of operations
