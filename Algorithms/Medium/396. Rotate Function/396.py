from typing import List

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
      curr = sum(i * k for i, k in enumerate(nums))
      N, sm, mx = len(nums), sum(nums), curr
      for n in reversed(nums):
        curr = curr + sm - N * n
        mx = max(mx, curr)
      return mx

# the idea is to use the fact that the maximum value of the function is the sum of the elements of the array multiplied by their indices
# we calculate the current value of the function
# we calculate the sum of the elements of the array
# we calculate the maximum value of the function
# we iterate through the array in reverse
# we update the current value of the function
# we update the maximum value of the function
