from typing import List
from itertools import product

class Solution:
  def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    dp = [i for i in range(m * n)]
    for i, j in product(range(m - 2, -1, -1), range(n)):
        dp[grid[i][j]] += min(moveCost[grid[i][j]][k] + dp[grid[i + 1][k]] for k in range(n))
    return min(dp[k] for k in grid[0])

# first, we get the dimensions of the grid
# we initialize a dp list with the range of the grid
# we iterate through the grid in reverse
# we update the dp list with the minimum move cost and the next move cost
# we return the minimum move cost of the first row
