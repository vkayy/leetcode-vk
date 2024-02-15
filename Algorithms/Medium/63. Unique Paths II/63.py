from typing import List
from functools import lru_cache

class Solution:
  def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    @lru_cache()
    def dp(i, j):
      if i == m - 1 and j == n - 1 and not obstacleGrid[i][j]:
        return 1
      if i >= m or j >= n or obstacleGrid[i][j]:
        return 0
      return dp(i + 1, j) + dp(i, j + 1)
    return dp(0, 0)
