from typing import List
from functools import product

class Solution:
  def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    def dfs(i, j):
      if not (0 <= i < m) or not (0 <= j < n) or grid[i][j] == 0:
        return 0
      grid[i][j] = 0
      return 1 + sum(dfs(i + x, j + y) for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)])
    return max(dfs(i, j) for i, j in product(range(m), range(n)))

# first, we define the dimensions of the grid
# then, we define a dfs function
# if the current cell is out of bounds or is 0, we return 0
# otherwise, we set the current cell to 0 to mark it as visited
# then, we return 1 + the sum of the dfs of the 4 adjacent cells
# we return the maximum dfs of all the cells in the grid
# this returns the maximum area of an island in the grid
