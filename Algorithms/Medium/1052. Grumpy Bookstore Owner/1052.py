from typing import List

class Solution:
  def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
    init = sum(0 if grumpy[i] else c for i, c in enumerate(customers))
    l, r = 0, 0
    cur, mx = 0, 0
    while r < len(customers):
      if grumpy[r]:
        cur += customers[r]
      if r - l + 1 >= minutes:
        mx = max(mx, cur)
        if grumpy[l]:
          cur -= customers[l]
        l += 1
      r += 1
    return init + mx

# first, we calculate the initial satisfaction
# then we move the window to the right, updating the current satisfaction
# if the window size is greater than or equal to minutes, we update the maximum satisfaction
# finally, we return the sum of the initial satisfaction and the maximum satisfaction
# this is because the initial satisfaction is the satisfaction without using the power
# and the maximum satisfaction is the satisfaction using the power
# therefore, the result is the sum of the initial satisfaction and the maximum satisfaction
