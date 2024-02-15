from typing import List
from functools import lru_cache

class Solution:
  def minimumTotal(self, triangle: List[List[int]]) -> int:
    h = len(triangle)
    @lru_cache(None)
    def dp(i, j):
      if i == h - 1:
        return triangle[i][j]
      if i >= h or j >= len(triangle[i]):
        return float("inf")
      return triangle[i][j] + min(dp(i + 1, j), dp(i + 1, j + 1))
    return dp(0, 0)

# we use dynamic programming to solve this problem
# we create a recursive function to calculate the minimum path sum
# we use memoization to optimize the recursive function
# we return the minimum path sum for the first cell
# if the pointer for the row reaches the end, we return the value of the current cell
# this is because we have reached the end of the triangle
# if the pointer for the row is out of bounds, we return infinity
# this is because we cannot find a path sum with the remaining rows
# we calculate the minimum path sum for each cell
