from typing import List

class Solution:
  def minPathSum(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    for i in range(m - 1, -1, -1):
      for j in range(n - 1, -1, -1):
        dp[i][j] = grid[i][j]
        if not (i == m - 1 and j == n - 1):
          dp[i][j] += min(dp[i + di][j + dj] for di, dj in [(0, 1), (1, 0)] if i + di < m and j + dj < n)
    return dp[0][0]

# we use dynamic programming to solve this problem
# we create a 2D array of the same size as the input grid
# we iterate through the grid in reverse order
# we calculate the minimum path sum for each cell
# we return the minimum path sum for the first cell
