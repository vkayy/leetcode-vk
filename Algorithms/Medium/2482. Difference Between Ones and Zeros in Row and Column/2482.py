from typing import List
from itertools import product

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        rows, cols = [], []
        for row in grid:
            rows.append(row.count(1))
        for col in zip(*grid):
            cols.append(col.count(1))
        for i, j in product(range(m), range(n)):
            grid[i][j] = rows[i] * 2 + cols[j] * 2 - m - n
        return grid

# first, we count the number of 1s in each row and column
# then, we use the formula
# we return the grid