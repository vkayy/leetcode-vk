from typing import List

class Solution:
  def minCost(self, colors: str, neededTime: List[int]) -> int:
    res, mx, cur = 0, -1, 0
    for i in range(len(colors)):
      cur += neededTime[i]
      mx = max(mx, neededTime[i])
      if i == len(colors) - 1 or colors[i] != colors[i + 1]:
        res += cur - mx
        mx, cur = -1, 0
    return res

# first, initialise res, mx, and cur to 0, -1, and 0
# res is the final result, mx is the maximum time, and cur is the current running sum

# then, we iterate through the indices of colors

# we increment cur by neededTime[i]
# this is because we want to find the total time in the current group
# we set mx to the maximum of mx and neededTime[i]
# this is because we want to find the maximum time in the current group

# if we are at the last index, or there is a colour change
# we increment res by cur - mx
# this is because we want to find the total time in the current group minus the maximum time in the current group
# we set mx and cur to -1 and 0
# this is because we want to reset mx and cur to their initial values

# finally, we return res