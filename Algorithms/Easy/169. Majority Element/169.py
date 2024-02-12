from typing import List

class Solution:
  def majorityElement(self, nums: List[int]) -> int:
    c = m = 0
    for n in nums:
      if c == 0:
        m, c = n, 1
      else:
        c = c + (1 if m == n else -1)
    return m

# this is the Boyer-Moore Voting Algorithm

# set the counter and the majority element to 0
# iterate through the array
# if the counter is 0, set the majority element to the current element and set the counter to 1
# otherwise, if the current element is the majority element, increment the counter by 1
# otherwise, decrement the counter by 1

# as the majority element appears more than n/2 times, it will always have a positive counter at the end of the iteration
