from typing import List

class Solution:
  def rearrangeArray(self, nums: List[int]) -> List[int]:
    return [n for pair in zip([x for x in nums if x > 0], [x for x in nums if x < 0]) for n in pair]

# first, we filter the positive and negative numbers into separate lists
# then, we zip the two lists together, creating a list of tuples
# finally, we flatten the list of tuples into a single list
