from typing import List

class Solution:
  def cherryPickup(self, grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    prev = [[grid[rows - 1][j] + (0 if j == k else grid[rows - 1][k]) for j in range(cols)] for k in range(cols)]
    for i in range(rows - 2, -1, -1):
      curr = [[0] * cols for _ in range(cols)]
      for j in range(min(i + 1, cols)):
        for k in range(max(j, cols - i - 1), cols):
          for dj, dk in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]:
            if 0 <= j + dj < k + dk < cols and prev[j + dj][k + dk] > curr[j][k]:
              curr[j][k] = prev[j + dj][k + dk]
          curr[j][k] += grid[i][j] + (0 if j == k else grid[i][k])
      prev = curr
    return prev[0][cols - 1]

# we store the maximum number of cherries that can be picked up by two robots starting at (i, j) and (i, k) at the same time in the 2D array prev
# we iterate through the rows from the second last row to the first row
# we use a 2D array curr to store the maximum number of cherries that can be picked up by two robots starting at (i, j) and (i, k) at the same time
# we iterate through the columns from 0 to min(i + 1, cols)
# we choose min(i + 1, cols) because the left robot can only move to the right i + 1 times
# we choose max(j, cols - i - 1) to cols because the right robot can only move to the left cols - i - 1 times
