from typing import List

class Solution:
  def cherryPickup(self, grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    dp = [[[grid[i][j] + (0 if j == k else grid[i][k]) for k in range(cols)] for j in range(cols)] for i in range(rows)]
    for i in range(rows - 2, -1, -1):
      for j in range(cols):
        for k in range(cols):
          dp[i][j][k] += max(dp[i + 1][j + dj][k + dk] for dj, dk in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)] if 0 <= i + 1 < rows and 0 <= j + dj < cols and 0 <= k + dk < cols)
    return dp[0][0][cols - 1]

# we use a 3D dp array to store the maximum number of cherries that can be picked up by two robots starting at (i, j) and (i, k) at the same time
