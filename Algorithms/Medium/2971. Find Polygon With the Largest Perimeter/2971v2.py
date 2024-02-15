from typing import List
from itertools import accumulate

class Solution:
  def largestPerimeter(self, nums: List[int]) -> int:
    return res[0] if ((srt := sorted(nums)) and (pref := list(accumulate(srt))) and (res := [pref[i - 1] + srt[i] for i in range(len(pref) - 1, 1, -1) if srt[i] < pref[i - 1]])) else -1

# this uses the prefix sum to find the highest perimeter
# if the highest perimeter is valid, return it
# if not, return -1
