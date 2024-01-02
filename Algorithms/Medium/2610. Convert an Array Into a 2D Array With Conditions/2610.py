from typing import List
from collections import defaultdict

class Solution:
  def findMatrix(self, nums: List[int]) -> List[List[int]]:
    count = defaultdict(int)
    res = []
    for num in nums:
      if count[num] >= len(res):
        res.append([])
      res[count[num]].append(num)
      count[num] += 1
    return res

# first, create dict to track freq of encountered nums
# then, create empty res list

# then, iterate through nums
# if the freq of the current num is greater than the length of the res list
# append an empty list to the res list
# append the current num to the list at the index of the freq of the current num
# increment the freq of the current num

# finally, return the res list