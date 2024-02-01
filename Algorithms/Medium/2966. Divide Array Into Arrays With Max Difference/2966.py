from typing import List

class Solution:
  def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
    nums.sort()
    res, cur = [[] for _ in range(len(nums) // 3)], 0
    for n in nums:
      if res[cur] and n - res[cur][0] > k:
        return []
      res[cur].append(n)
      if len(res[cur]) == 3:
        cur += 1
    return res

# first, sort the array
# then, initialise an empty array of arrays for each triplet
# then, initialise a pointer to the first array

# iterate through the sorted array
# if the current number is more than k away from the first number in the current array, return []
# otherwise, add the current number to the current array
# if the current array has 3 numbers, increment the pointer

# return the array of arrays
